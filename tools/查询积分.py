#!/usr/bin/env python3
# coding:utf-8

import os
import sys
import django
import datetime
from django.conf import settings
sys.path.append(os.path.abspath(".."))
os.chdir(os.path.abspath(".."))
os.environ['DJANGO_SETTINGS_MODULE'] = 'muchang_live.settings'
django.setup()
from danmaku.tools import *

a=User.objects.all()
x={}
for i in a:
    x[i.name]=i.gold

num = 0
l = sorted(x.items(),key=lambda x:x[1],reverse=True)
for i in l:
    num=num+1
    if i[0] == '勤劳的牧场主' or i[0] == '起源的大地':
        pass
    else:
        print(str(num) + '  ' + i[0] + ' : ' + str(i[1]))

os.system("pause")
