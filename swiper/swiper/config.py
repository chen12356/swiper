"""
本文件 主要 配置第三方接口的配置信息
"""

#云之讯短信平台配置
YZX_SMS_API = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_SMA_ARGS = {

    "sid":"5f6da1d7de0ef66861baba1acb2f16e5",
    "token":"880cf44120477c017719879e5923b9d5",
    "appid":"d4bc9ff2c1c0402084ea9854503d2fa6",
    "templateid":"518690",
    "param": None,  #  发送验证码内容
    "mobile": None,  # 接收手机号
}


#七牛云配置
QN_AK = "NgSX0tJ0uzqKlL_zMkLeqbnFX7MWTn7lLjvzvYLe"
QN_SK = "FV4S3xBqeJnT_h5NHx-RhEOfy5qVpH0dY32EtTqu"
QN_BUCKET_NAME = "swiper1"
QN_BASE_URL = " http://q1pprssob.bkt.clouddn.com"