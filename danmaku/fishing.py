# fishing
import random
import datetime
from danmaku.models import fish

def fish_list():
    f=[]
    for i in fish.objects.all():
        f.append(i)
    return(f)

def season():
    if 4 <= datetime.date.today().month <= 6 :
        season='spring'
    elif 7 <= datetime.date.today().month <= 9 :
        season='summer'
    elif 10 <= datetime.date.today().month <= 12 :
        season='autumn'
    elif 1 <= datetime.date.today().month <= 3 :
        season='winter'
    return season

def rd(num):
    i = random.randint(1,100)
    if i <= num:
        return True
    else:
        return False

def successful(f):
    if f.king == True:
        return rd(3)
    elif f.name in ["海贼宝藏","古代鱼化石","力之果实"]:
        return rd(20)
    elif f.name in ["鱼骨头","空罐子","长靴"]:
        return True
    elif f.name in ["河童","装有信的瓶子"]:
        return rd(1)
    else:
        return rd(98)

def random_fish():
    fishlist = fish_list()
    f = random.choice(fishlist)
    while season() not in f.season.split() :
        f = random.choice(fishlist)
    if successful(f) == True :
        size = 0
        s='贵重物品'
        if f.name in ["鱼骨头","空罐子","长靴"]:
            s='杂物'
            gold=1
        elif f.name == "海贼宝藏" :
            gold=10000
        elif f.name == "古代鱼化石" :
            gold=5000
        elif f.name == "装有信的瓶子" :
            gold=60000
        elif f.name == "河童" :
            s='河童'
            gold=0
        elif f.name == "力之果实" :
            s='力之果实'
            gold=0
        else:
            size = random.randint(f.size_min,f.size_max)
            if size <= 24:
                s='小鱼'
                gold=50
            elif 25 <= size <= 49:
                s='中鱼'
                gold=120
            elif size >= 50:
                s='大鱼'
                gold=200
        if f.king == True:
            gold=100000
        return (f.name,size,s,gold,f.king)
    else:
        return False

