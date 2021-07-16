#!/usr/bin/env python3
# coding:utf-8

import json
with open('fish.json','r',encoding='utf8')as x:
    f = json.load(x)

import os
import sys
import django
from django.conf import settings
sys.path.append('C:\\Users\\Misaka\\Desktop\\3472667\\muchang_live')
os.chdir('C:\\Users\\Misaka\\Desktop\\3472667\\muchang_live')
os.environ['DJANGO_SETTINGS_MODULE'] = 'muchang_live.settings'
django.setup()

# 清空
from danmaku.models import fish
fish.objects.all().delete()

# fish
from danmaku.models import fish
for i in f:
    a = fish(
        name = f[i]['name'],
        size_min = f[i]['size_min'],
        size_max = f[i]['size_max'],
        size = f[i]['size'],
        level = f[i]['level'],
        season = f[i]['season'],
        king = f[i]['king']
        )
    a.save()
