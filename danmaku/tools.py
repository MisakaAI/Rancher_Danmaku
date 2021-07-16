#!/usr/bin/env python3
# coding:utf-8

from danmaku.models import User
from danmaku.fishing import random_fish
import datetime

# 日志
def log(user,text):
    user.log = user.log + datetime.datetime.now().ctime() + ": " + str(text) + "\n"
    user.save()

# 创建用户
def add(uid,name):
    try:
        a = User(uid=uid, name=name)
        a.save()
        return('创建用户「' + name + '」成功,UID为' + str(uid) )
    except Exception as e:
        return('创建用户「' + name + '」失败,UID为' + str(uid) )

# 查找用户
def search(uid=False,name=''):
    try:
        if type(uid) == int:
            user = User.objects.get(uid=uid)
            #print('查找用户' + str(user.uid) + '成功。' )
            if name != '' and name != user.name :
                user.name = name
                log_info = '昵称修改为: ' + user.name
                log(user,log_info)
                user.save()
        elif name != '':
            user = User.objects.get(name=name)
            #print('查找用户' + user.name + '成功。' )
        return user
    except Exception as errot :
        #print('用户' + name + '不存在。\n\n' + str(errot) )
        return None

# 体力回复
def heal(name,value:int):
    try:
        user = search(name=name)
        if user.physical + value > 100:
            user.physical = 100
        else:
            user.physical = user.physical + value
        user.save()
        return True
    except:
        return False

# 完全回复
def heal_all():
    try:
        for i in User.objects.all():
            heal(i.name,100)
        return True
    except:
        return False

# 签到
def signin(user,vip):
    if user.sign_in != datetime.date.today():
        if vip == True:
            user.gold += 1000
        else:
            user.gold += 500
        user.sign_in = datetime.date.today()
        user.save()
        return True
    else:
        return False

# 命令
def command(user,danmu,vip,svip):
    if danmu == '签到':
        if signin(user,vip) == True:
            return("签到成功！")
        else :
            return("已签到！")
    elif danmu == '积分':
        return("的积分：" + str(user.gold))
    elif danmu == '体力':
        return("的体力：" + str(user.physical))
    elif danmu == '钓鱼':
        if user.physical >= 5:
            if vip == True:
                user.physical = user.physical - 5
            else :
                if user.physical >= 10:
                    user.physical = user.physical - 10
                else:
                    return('体力不足，无法钓鱼。')
            fish = random_fish()
            if fish == False:
                user.save()
                return('在钓鱼，但是没有钓起来……')
            else:
                user.gold = user.gold + fish[3]
                if fish[0] not in user.collect.split():
                    user.collect = user.collect + fish[0] + ' '
                user.save()
                if fish[4] == True:
                    return("钓起了" + fish[0] + "，是鱼王！还是放回去吧~")
                else:
                    if fish[1] == 0:
                        if fish[2] == '贵重物品':
                            info = '，好开心啊！'
                        elif fish[2] == '杂物':
                            info = '。保护环境，人人有责！'
                        elif fish[2] == '河童':
                            info = '，？？？'
                        elif fish[2] == '力之果实':
                            user.physical=100
                            user.save()
                            info = '，体力回复满了。'
                        else:
                            info = '，这是什么？'
                        return("钓起了" + fish[0] + info)
                    else :
                        return("钓起了" + fish[0] + "，长度为" + str(fish[1]) + "cm（" + fish[2] + "）")
        else:
            return('体力不足，无法钓鱼。')
    elif danmu == '一键钓鱼':
        if user.name == '勤劳的牧场主' or svip == True:
            if user.physical >= 5:
                fishes = {}
                while user.physical >= 5:
                    user.physical = user.physical - 5
                    fish = random_fish()
                    if fish == False:
                        while fish == False:
                            fish = random_fish()
                    user.gold = user.gold + fish[3]
                    if fish[0] not in user.collect.split():
                        user.collect = user.collect + fish[0] + ' '
                    if fish[2] == '力之果实':
                        user.physical=100
                    if fish[4] == True:
                        if fish[0] + '(鱼王)' in fishes:
                            fishes[fish[0] + '(鱼王)']+=1
                        else: 
                            fishes[fish[0] + '(鱼王)']=1
                    else:
                        if fish[0] in fishes:
                            fishes[fish[0]]+=1
                        else: 
                            fishes[fish[0]]=1
                user.save()
                fish_return = ''
                for i in fishes:
                    if fishes[i] != 1:
                        fish_return= fish_return + i + '×' + str(fishes[i]) + ', '
                    else:
                        fish_return= fish_return + i + ', '
                return("钓起了" + fish_return[:-2])
            else:
                return('体力不足，无法钓鱼。')
        else:
            return('没有权限使用该命令。')
    elif '回复' in danmu:
        if user.uid == 4516259:
            if danmu == '完全回复':
                try:
                    heal_all()
                    user.physical=100
                    user.save()
                    return '使用了完全回复，所有人的体力都满了'
                except:
                    return '完全回复失败'
            if danmu == '回复':
                user.physical = 100
                user.save()
                return '的体力回满了。'
            else:
                d = danmu.split()
                if d[1] == user.name:
                    user.physical = user.physical + int(d[2])
                    user.save()
                    return '回复了自己' +  d[2] + '体力'
                else:
                    heal(d[1],int(d[2]))
                    return '回复了' + d[1] + d[2] + '体力'
        else:
            if danmu[2:].isdigit() == True:
                heal_add = int(danmu[2:])
                if user.physical + heal_add > 100:
                    heal_add = 100 - user.physical
            elif danmu == '回复':
                heal_add = 100 - user.physical
            heal_gold = 10
            if user.gold > heal_add * heal_gold :
                user.gold = user.gold - heal_add * heal_gold
                user.physical = user.physical + heal_add
                user.save()
                return '回复了' + str(heal_add) + '体力, 扣除' + str(heal_add * heal_gold) + '积分'
            else:
                return '积分不足，无法回复体力'
    elif  danmu == 'xx':
        pass
    else:
        return '使用的命令不存在。'
