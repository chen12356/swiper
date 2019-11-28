'''
本文件主要是编写其他功能的逻辑代码
'''
import random

import requests
from django.core.cache import cache

from swiper import config
def get_random_code(length=6):
    """
    生成指定长度随机验证码
    :param length: 默认长度 6 位
    :return: 返回为 6位验证码  类型：str
    """
    return "".join([str(random.randint(0,9)) for i in range(length)])

def send_vcode(phone):
    """
    给指定手机发送短信验证码
    :param phone: 用户手机号
    :return: 布尔值（True 成功、False 失败）
    """
    vcode = get_random_code()
    args = config.YZX_SMA_ARGS.copy() # 浅拷贝全局的配置，防止多个用户同时操作，导致可变数据类型(这里该字典)发生变化
    # 添加发送数据
    args['param'] = vcode
    #添加接收手机号
    args['mobile'] = phone

    #请求云之讯平台第三方接口
    response = requests.post(config.YZX_SMS_API,json=args)
    if response.status_code == 200:
        result = response.json()   #转成json数据
        print(result)
        if result['msg'] == 'OK':
            # 设置到缓存中：本项目缓存到redis中,过期时间300s，注意：设置的key名尽可能顾名思义
            cache.set("vcode-%s" % phone,vcode,timeout=3000)
            return True
    return False