from django.shortcuts import render

# Create your views here.


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import AlbumInfo


def album(request, id, page):
    albumList = AlbumInfo.objects.filter(user_id=id).order_by('id')
    paginator = Paginator(albumList, 8)
    try:
        pageInfo = paginator.page(page)
    except PageNotAnInteger:
        # if type of parameter 'page' is not an integer, return page 1
        pageInfo = paginator.page(1)
    except EmptyPage:
        # if page visited by user is out of range, return last page
        pageInfo = paginator.page(paginator.num_pages)
    return render(request, 'album.html', locals())