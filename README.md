# 牧场主の弹幕姬

## 依赖

``` sh
# Python3
pip install django
pip install bilibili-api
```

## 模型

### 用户

属性|名称|类型
-|-|-
uid|B站UID|整数
name|B站昵称|字符串
gold|金钱|整数
physical|体力|整数
first_time|首次登录时间|时间
last_time|最后登录时间|时间
sign_in|签到时间|时间
log|日志|文本
collect|图鉴|文本

### 鱼

属性|名称|类型
-|-|-
name|名称|字符串
size_min|最小尺寸|整数
size_max|最大尺寸|整数
size|尺寸|字符串
level|蓄力等级|整数
season|季节|字符串
king|鱼王|布尔值