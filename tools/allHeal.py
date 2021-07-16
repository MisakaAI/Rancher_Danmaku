#!/usr/bin/env python3
# coding:utf-8

import os
import sys
import django
from django.conf import settings
sys.path.append(os.path.abspath(".."))
os.chdir(os.path.abspath(".."))
os.environ['DJANGO_SETTINGS_MODULE'] = 'muchang_live.settings'
django.setup()
from danmaku.tools import heal_all
heal_all()
