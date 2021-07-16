from django.db import models
import datetime
# Create your models here.

class User(models.Model):
    # 属性
    uid = models.BigIntegerField(verbose_name='UID')
    name = models.CharField(max_length=100,verbose_name='昵称')
    gold = models.BigIntegerField(default=0,verbose_name='金钱')
    physical = models.BigIntegerField(default=100,verbose_name='体力')
    first_time = models.DateField(auto_now_add=True,verbose_name='首次登录时间')
    last_time = models.DateField(auto_now=True,verbose_name='最后登录时间')
    sign_in = models.DateField(default=datetime.date.min, verbose_name='签到时间')
    log = models.TextField(default='', verbose_name='日志')
    collect = models.TextField(default='', blank=True, verbose_name='图鉴')
    # def knapsack_default():
    #     return {
    #         "1": '', # 背包 1
    #         "2": '', # 背包 2
    #         "3": '', # 背包 3
    #         "4": '', # 背包 4
    #         "5": '', # 背包 5
    #         "6": '', # 背包 6
    #     }
    # def tool_default():
    #     return {
    #         "Hoe": 1, # 锄头
    #         "Sprinkler": 1, # 洒水器
    #         "Sickle": 1, # 镰刀
    #         "Hammer": 1, # 锤子
    #         "Axe": 1, # 斧头
    #         "fishing_rod": 0, # 钓鱼竿
    #     }
    # knapsack = models.JSONField(default=knapsack_default,verbose_name='背包')
    # tool = models.JSONField(default=tool_default,verbose_name='工具')
    # # 动物
    # animal_house
    # chicken_house

    # {
    #     {
    #         'name':'',
    #         'egg':'',
    #         'favors':''
    #     }
    # }
    # chicken_1
    # chicken_2
    # chicken_3
    # chicken_4
    # chicken_5
    # chicken_6

class fish(models.Model):
    name = models.CharField(max_length=100,verbose_name='名称')
    size_min = models.IntegerField(verbose_name='最小尺寸')
    size_max = models.IntegerField(verbose_name='最大尺寸')
    size = models.CharField(blank=True,max_length=100,verbose_name='尺寸')
    level = models.IntegerField(verbose_name='蓄力等级')
    season = models.CharField(max_length=100,verbose_name='季节')
    king = models.BooleanField(default=False,verbose_name='鱼王')
