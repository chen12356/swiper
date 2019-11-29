from qiniu import Auth, put_file, etag
from swiper import config

def upload_to_qiniu(filename,filepath):
    #构建鉴权对象
    q = Auth(config.QN_AK, config.QN_SK)

    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(config.QN_BUCKET_NAME, filename, 3600)
    #上传图片
    put_file(token,filename,filepath)
    #图片的url
    url = "%s/%s" %(config.QN_BASE_URL,filename)
    return url