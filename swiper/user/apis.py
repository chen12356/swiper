from django.http import JsonResponse
from django.core.cache import cache

# Create your views here.
from swiper.common import stat
from swiper.user import logics
from swiper.user.models import User, Profile


def get_vcode(request):
    """点击获取验证码-->用户会收到信息"""
    phonenum = request.GET.get('phonenum')
    status = logics.send_vcode(phonenum)
    if status:
        # 返回的状态码--> 规定的 stat里面状态码的变量
        return JsonResponse({'code':stat.OK,'data':None})
    return JsonResponse({'code':stat.VCODE_ERR,'data':None})

def submit_vcode(request):
    """通过验证码和手机 登录"""
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    #获取缓存的验证码
    cache_code = cache.get("vcode-%s" % phonenum)
    if vcode and vcode == cache_code:
        try:
            # 查找用户
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum)  # create 直接创建用户，因为其他字段均设置了默认值

        #执行登陆过程--> 将用户id保存在session中
        request.session['uid'] = user.id
        return JsonResponse({'code':stat.OK,'data':user.to_dict()})
    return JsonResponse({'code':stat.VCODE_ERR,'data':'验证失败'})

def get_profile(request):
    """获取个人资料"""
    #需要获取当前的 用户的id--> 那么需要去session里面去，可以知道：其他的模块肯定会用到uid
    # 利用中间件去处理，获取uid，对每个页面都进行判断，(路由分发前判断)

    #获取uid，如果是新创建的，那么需要先存入数据库，在读取，如果已经存在了，那么直接读取
    profile, _ = Profile.objects.get_or_create(id=request.uid)
    return JsonResponse({'code':stat.OK,'data':profile.to_dict()})