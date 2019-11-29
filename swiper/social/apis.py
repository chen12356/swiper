# Create your views here.

from libs.http import render_json

def rcmd_users(request):
    """推荐用户接口"""
    return render_json()

def like(request):
    """右滑：喜欢"""

    return render_json()


def superlike(request):
    """上滑：超级喜欢"""

    return render_json()


def dislike(request):
    """左滑：不喜欢"""

    return render_json()


def rewind(request):

    return render_json()


def who_like_me(request):

    return render_json()


def friend_list(request):

    return render_json()