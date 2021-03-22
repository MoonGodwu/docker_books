from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.
from app01 import models





def author_list(request):
    authors = models.Author.objects.all()
    models.Author.objects.all().annotate()
    return render(request, 'author_list.html', {'author_list': authors})


def publish_list(request):
    publishs = models.Publish.objects.all()
    return render(request, 'publish_list.html', {'publish_list': publishs})


def author_delete(request):
    id = request.GET.get('id')
    ret = models.Author.objects.filter(pk=id).delete()
    return redirect('/author_list/')
    # 不要用这个
    # return render(request,'author_list.html')


def author_update(request, nid):
    if request.method == 'GET':
        author = models.Author.objects.get(pk=nid)
        return render(request, 'author_update.html', locals())
    else:
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        models.Author.objects.filter(pk=nid).update(name=name, sex=sex)
        return redirect('/author_list/')


def author_add(request):
    if request.method == 'GET':
        return render(request, 'author_add.html')
    else:
        name=request.POST.get('name')
        sex=request.POST.get('sex')
        models.Author.objects.create(name=name,sex=sex)

        return redirect('/author_list/')


def error(request):
    return HttpResponse('404')
