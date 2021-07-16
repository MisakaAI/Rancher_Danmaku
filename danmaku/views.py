from django.shortcuts import render,redirect
from danmaku.tools import *
# Create your views here.
from django.http import HttpResponse

def ranklist(request):
    if request.method == 'POST':
        id = request.POST['id']
        if id != '':
            return redirect('/id/' + id)
    else:
        a=User.objects.all()
        x={}
        for i in a:
            x[i.name]=i.gold

        num = 0
        l = sorted(x.items(),key=lambda x:x[1],reverse=True)
        text=[]
        for i in l:
            num=num+1
            if i[0] == '勤劳的牧场主' or i[0] == '起源的大地':
                num=num-1
                pass
            else:
                text.append([i[0],format(i[1],",")])
        
        context = {
            "title" : '牧场主の积分榜',
            "text" : text
        }
        return render(request, 'ranklist.html', context)

all_fish = ['大泷六线鱼','竹荚鱼','拉氏大吻鱥','马苏钩吻鲑','黄鸡鱼','沙丁鱼','鳟鱼','珠星三块鱼','鳗鱼','日本溪哥','鲣鱼','鲽鱼','剥皮鱼','鲫鱼','兰氏鲫','褐带石斑鱼','大头鱼','鲑鱼','青花鱼','水针鱼','马蛟鱼','秋刀鱼','鬼头刀','鲷鱼','鳕鱼','泥鳅','沙塘鳢','虹鳟','鲱鱼','鲢鱼','日本叉牙鱼','比目鱼','河豚','黑鲈鱼','鰤鱼','蓝腮太阳鱼','日本白鲫','远东哲罗鱼','黑鲔鱼','曼波鱼','狮子鱼','无备平鮋','山女鳟','雷鱼','西太公鱼','白带鱼','香鱼','沙鮻','狼牙鳝']
all_king = ['鮟鱇鱼','乌贼','伊富鱼','温泉鲇鱼','鲤鱼','腔棘鱼','巨骨舌鱼']
all_rare = ['古代鱼化石','海贼宝藏']
all_legend = ['河童','装有信的瓶子']

def name(request, name):
    user = search(name=name)
    if user != None :
        log=[]
        for i in user.log.split('\n')[-100:]:
            log.append(i)
        log.remove("")
        log.reverse()
        fish = user.collect.split()
        context = {
            "title" : user.name,
            'ID':user.id,
            'UID':user.uid,
            'name':user.name,
            'gold':user.gold,
            'physical':user.physical,
            'heart':range(user.physical//10),
            'half':user.physical/5%2 == 0,
            'heart_is_zero':user.physical//10==0,
            'log':log,
            'fish':fish,
            'all_fish':all_fish,
            'all_king':all_king,
            'all_rare':all_rare,
            'all_legend':all_legend
        }
        return render(request, 'user.html', context)
    else :
        return HttpResponse('用户【' + name + '】不存在')

def documentation(request):
    context = {
        "title" : '弹幕姬の文档',
    }
    return render(request, 'documentation.html', context)

def about(request):
    context = {
        "title" : '关于本站',
    }
    return render(request, 'about.html', context)