
from django.core.cache import cache

# Create your views here.
from common import stat
from user.models import User, Profile
from libs.http import render_json
# from libs.qn_cloud import upload_to_qiniu
from user import logics

from user.forms import UserForm, ProfileForm


def get_vcode(request):
    """点击获取验证码-->用户会收到信息"""
    phonenum = request.GET.get('phonenum')
    status = logics.send_vcode(phonenum)
    if status:
        # 返回的状态码--> 规定的 stat里面状态码的变量
        return render_json()
    return render_json(code=stat.VCODE_ERR)

def submit_vcode(request):
    """通过验证码和手机 登录"""
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    #获取缓存的验证码
    cache_code = cache.get("vcode-%s" % phonenum)
    print(cache_code)
    if vcode and vcode == cache_code:
        try:
            # 查找用户
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum)  # create 直接创建用户，因为其他字段均设置了默认值

        #执行登陆过程--> 将用户id保存在session中
        request.session['uid'] = user.id
        return render_json(user.to_dict())
    return render_json(code=stat.VCODE_ERR)

def get_profile(request):
    """获取个人资料"""
    #需要获取当前的 用户的id--> 那么需要去session里面去，可以知道：其他的模块肯定会用到uid
    # 利用中间件去处理，获取uid，对每个页面都进行判断，(路由分发前判断)

    #获取uid，如果是新创建的，那么需要先存入数据库，在读取，如果已经存在了，那么直接读取
    profile, _ = Profile.objects.get_or_create(id=request.uid)
    return render_json(profile.to_dict())

def set_profile(request):
    '''修改个人资料'''
    user_form = UserForm(request.POST)
    profile_form = ProfileForm(request.POST)

    #检查 数据 有效性
    if not user_form.is_valid():
        return render_json(user_form.errors,stat.USER_FORM_ERR)
    if not profile_form.is_valid():
        return render_json(profile_form.errors,stat.PROFILE_FORM_ERR)

    #保存数据   利用update方法，进行更新--> 参数：字段=值 --> 这里用 ** 拆包字典，一次性传过去
    User.objects.filter(id=request.uid).update(**user_form.cleaned_data)
    Profile.objects.filter(id=request.uid).update(**profile_form.cleaned_data)

    return render_json()
def upload_avatar(request):
    avatar_file = request.FILES.get('avatar')
    print(avatar_file)
    logics.upload_avatar.delay(request.uid,avatar_file)
    # filename,filepath = logics.save_avatar(request.uid,avatar_file) #保存到本地
    # avatar_url = upload_to_qiniu(filename,filepath)  # 上传到七牛云，同时得到远程图片的url
    # User.objects.filter(id=request.uid).update(avatar=avatar_url) # 保存到数据库中
    # os.remove(filepath) #删除本地临时文件
    return render_json()