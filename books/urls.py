"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01.view import author
from app01.view import book
from app01.view import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', book.index),
    url(r'^book_list/$', book.book_list,name='book_list'),
    url(r'^book_delete/(?P<id>\d+)$', book.book_delete,name='book_delete'),
    url(r'^book_update/(?P<id>\d+)$', book.book_update),
    url(r'^book_add/$', book.book_add),
    url(r'^author_list/$', author.author_list),
    url(r'^publish_list/$', author.publish_list),
    url(r'^author_delete/$', author.author_delete),
    url(r'^author_add/$', author.author_add),
    url(r'^author_update/(\d+)$', author.author_update),
    url(r'^author_update/', author.author_update,{'id':1}),


    url(r'', views.error),

]
