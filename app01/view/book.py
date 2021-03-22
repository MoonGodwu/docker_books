
from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.
from app01 import models


def index(request):

    return render(request,'index.html')
def book_list(request):
    book_list = models.Book.objects.all()
    # print(book_list[0].pub_date)
    return render(request, 'book_list.html', {'book_list': book_list})


def book_delete(request, id):
    try:
        models.Book.objects.get(pk=id).delete()
    except Exception as e:
        print(e)
    url = reverse('book_list')
    return redirect(url)


def book_add(request):
    if request.method == 'GET':
        authors = models.Author.objects.all()
        publish_list = models.Publish.objects.all()
        return render(request, 'book_add.html', locals())
    else:
        name = request.POST.get('name')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        # 传过多个作者,所以用getlist取
        authors = request.POST.getlist('authors')
        publish = request.POST.get('publish')
        book = models.Book.objects.create(name=name, price=price, pub_date=pub_date, publish_id=publish)
        # 创建书跟作者的关联关系
        book.authors.add(*authors)
        return redirect('/book_list/')


def book_update(request, id):
    if request.method == 'GET':
        book = models.Book.objects.get(pk=id)
        print(book.pub_date)
        print(book.authors.all())
        authors = models.Author.objects.all()
        publish_list = models.Publish.objects.all()
        return render(request, 'book_update.html', locals())
    else:
        name = request.POST.get('name')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        authors = request.POST.getlist('authors')
        publish = request.POST.get('publish')
        # 第一种方式.还有第二种
        book = models.Book.objects.get(pk=id)
        book.name = name
        book.price = price
        book.pub_date = pub_date
        book.publish_id = publish
        book.save()
        # 修改作者(第一种方式,还有第二种)
        book.authors.clear()
        book.authors.add(*authors)

        return redirect('/book_list/')