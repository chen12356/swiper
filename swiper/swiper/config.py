"""
本文件 主要 配置第三方接口的配置信息
"""

#云之讯短信平台配置
YZX_SMS_API = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_SMA_ARGS = {
    "sid": "2ff56f07e2d002ab9900777dd4b09edf",
    "token": "d763718424035afc347cbd3bba3813a2",
    "appid": "8235102f41ed4603802b05264c59430e",
    # "sid":"5f6da1d7de0ef66861baba1acb2f16e5",
    # "token":"",
    # "appid":"d4bc9ff2c1c0402084ea9854503d2fa6",
    "templateid": "503617",
    "param": None,  #  发送验证码内容
    "mobile": None,  # 接收手机号
}
