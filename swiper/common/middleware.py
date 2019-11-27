from  django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

from swiper.common import stat

class AuthMiddleware(MiddlewareMixin):
    #用户登陆验证的中间件，在一些接口验证用户是否登陆

    #创建白名单：有些页面并不需要验证
    path_white_list = [
        'api/user/get_vcode',
        'api/user/submit_vcode',
    ]

    def process_request(self,request):
        if request.path not in self.path_white_list:
            uid = request.session.get('uid')
            if not uid:
                return JsonResponse({'code':stat.LOGIN_REQUIRED,'data':'用户未登陆'})
            else:
                request.uid = uid    #给request添加uid属性，，动态添加，这样其他接口，获取uid就简单了