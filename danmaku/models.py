from django.db import models
import datetime
# Create your models here.

class User(models.Model):
    uid = models.BigIntegerField(verbose_name='UID')
    name = models.CharField(max_length=100,verbose_name='昵称')
    gold = models.BigIntegerField(default=0,verbose_name='积分')
    physical = models.BigIntegerField(default=100,verbose_name='体力')
    physical_max = models.BigIntegerField(default=100,verbose_name='体力上限')
    fruit = models.TextField(default='', blank=True, verbose_name='力之果实')
    first_time = models.DateField(auto_now_add=True,verbose_name='首次登录时间')
    last_time = models.DateField(auto_now=True,verbose_name='最后登录时间')
    sign_in = models.DateField(default=datetime.date.min, verbose_name='签到时间')
    log = models.TextField(default='', blank=True, null = True, verbose_name='日志')
    collect = models.TextField(default='', blank=True, verbose_name='图鉴')
class fish(models.Model):
    name = models.CharField(max_length=100,verbose_name='名称')
    size_min = models.IntegerField(verbose_name='最小尺寸')
    size_max = models.IntegerField(verbose_name='最大尺寸')
    size = models.CharField(blank=True,max_length=100,verbose_name='尺寸')
    level = models.IntegerField(verbose_name='蓄力等级')
    season = models.CharField(max_length=100,verbose_name='季节')
    king = models.BooleanField(default=False,verbose_name='鱼王')
