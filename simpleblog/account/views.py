from django.shortcuts import render

# Create your views here.


from django.shortcuts import redirect
from .models import BlogUser
from album.models import AlbumInfo
from article.models import ArticleTag
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse


def register(request):
    title = '注册博客'
    pageTitle = '用户注册'
    confirmPassword = True
    button = '注册'
    urlText = '用户登录'
    urlName = 'userLogin'
    tips = ''
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password', '')
        cp = request.POST.get('cp', '')
        if BlogUser.objects.filter(username=u):
            tips = '用户已存在'
        elif cp != p:
            tips = '两次密码输入不一致'
        else:
            d = {
                'username': u,
                'password': p,
                'is_superuser':0,
                'is_staff':1
            }
            user = BlogUser.objects.create_user(**d)
            user.save()
            tips = '注册成功，请登录'
            logout(request)
            return redirect(reverse('userLogin'))
    return render(request, 'user.html', locals())

def userLogin(request):
    title = '登录博客'
    pageTitle = '用户登录'
    button = '登录'
    urlText = '用户注册'
    urlName = 'register'
    tips = ''
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password', '')
        if BlogUser.objects.filter(username=u):
            user = authenticate(username=u, password=p)
            if user:
                if user.is_active:
                    login(request, user)
                    kwargs = {'id': request.user.id, 'page': 1}
                    return redirect(reverse('article', kwargs=kwargs))
                else:
                    tips = '账号密码错误，请重新输入'
            else:
                tips = '用户不存在，请注册'
        else:
            if request.user.username:
                kwargs = {'id': request.user.id, 'page': 1}
                return redirect(reverse('article', kwargs=kwargs))
    return render(request, 'user.html', locals())

def about(request, id):
    album = AlbumInfo.objects.filter(user_id=id)
    tag = ArticleTag.objects.filter(user_id=id)
    user = BlogUser.objects.filter(id=id).first()
    return render(request, 'about.html', locals())