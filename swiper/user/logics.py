'''
本文件主要是编写其他功能的逻辑代码
'''
import random
import os
import requests
from django.core.cache import cache

from swiper import config
from user.models import User
from libs.qn_cloud import upload_to_qiniu
from tasks import celery_app
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
            cache.set("vcode-%s" % phone,vcode,timeout=30000)
            return True
    return False

def save_avatar(uid, avatar_file):
    '''将个人形象保存到本地'''
    filename = 'Avatar-%s' % uid  #拼接文件名
    filepath = '/tmp/%s' % filename  #保存到本地的临时文件
    with open(filepath, 'wb') as fp:
        for chunk in avatar_file.chunks():
            fp.write(chunk)
    return filename, filepath

#利用celery消息队列来除处理耗时的操作，比如用户服务器接收到客户头像，那么后续的
#过程交给celery来 处理
#该装饰后的函数，该函数被调用的的时候需要加 函数.delay(参数)  --》delay() 会使celery生效
    # 先启动 celery任务，然后在启动django项目
        # celery启动命令： celery worker -A 模块名(这里为 tasks) --loglevel=info
@celery_app.task
def upload_avatar(uid,avatar_file):
    filename,filepath = save_avatar(uid,avatar_file) #保存到本地
    avatar_url = upload_to_qiniu(filename,filepath)  # 上传到七牛云，同时得到远程图片的url
    User.objects.filter(id=uid).update(avatar=avatar_url) # 保存到数据库中
    os.remove(filepath) #删除本地临时文件
