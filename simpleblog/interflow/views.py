from django.shortcuts import render

# Create your views here.


from django.shortcuts import redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from article.models import ArticleTag
from account.models import BlogUser
from album.models import AlbumInfo
from .models import Board
from django.urls import reverse


def board(request, id, page):
    album = AlbumInfo.objects.filter(user_id=id)
    tag = ArticleTag.objects.filter(user_id=id)
    user = BlogUser.objects.filter(id=id).first()
    if not user:
        return redirect(reverse('register'))
    if request.method == 'GET':
        boardList = Board.objects.filter(user_id=id).order_by('-created')
        paginator = Paginator(boardList, 10)
        try:
            pageInfo = paginator.page(page)
        except PageNotAnInteger:
            # if type of parameter 'page' is not an integer, return page 1
            pageInfo = paginator.page(1)
        except EmptyPage:
            # if page visited by user is out of range, return last page
            pageInfo = paginator.page(paginator.num_pages)
        return render(request, 'board.html', locals())
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        value = {
            'name': name,
            'email': email,
            'content': content,
            'user_id': id
        }
        Board.objects.create(**value)
        kwargs = {'id': id, 'page': 1}
        return redirect(reverse('board', kwargs=kwargs))