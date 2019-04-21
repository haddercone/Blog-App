from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from posts.models import Auther , Content
from django.utils import timezone
def details(request):
    auther = Auther.objects.order_by('-pub_date')[:4]
    all_auther = Auther.objects.order_by('-pub_date')
    context = {
        'auther':auther,
        'all_auther':all_auther,
    }
    return render(request , 'posts/index.html',context)

def post_detail(request,pk):
    detail = Auther.objects.get(pk = pk)
    content = get_object_or_404(Content , pk = pk)

    context = {
        'detail':detail,
        'content':content,
    }
    return render(request, 'posts/post_detail.html',context)