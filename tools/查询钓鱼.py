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

for i in a:
    z=[]
    for x in i.log.split('\n'):
        if '鱼王' in x:
            z.append(x)
        elif '开心' in x:
            z.append(x)
    if z != []:
        print('-----------------')
        print(i.name + '\n')
        for y in z:
            print(y)
print('-----------------')

os.system("pause")