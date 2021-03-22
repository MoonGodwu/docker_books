from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

# 用了OneToOneField和ForeignKey,模型表的字段,后面会自定加_id
# ManyToManyField会自动创建第三张表
# *************重点
# 一对一的关系:OneToOneField
# 一对多的关系:ForeignKey
# 多对多的关系:ManyToManyField


class Publish(models.Model):
    # id如果不写,会自动生成,名字叫nid,并且自增
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    email = models.EmailField()


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    # 数字类型
    sex = models.CharField(max_length=32)
    # 可以用ForeignKey,但是得设置唯一性约束,会报警告,不建议用,建议用OneToOneField
    # authordetail=models.ForeignKey(unique=True)
    # to='AuthorDetail'  加引号,这个表能找到就可以,不用引号,类必须在上面定义
    authordetail = models.OneToOneField(to='AuthorDetail', to_field='id', null=True)

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, db_index=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField(auto_now_add=True)
    publish = models.ForeignKey(to=Publish, to_field='id', on_delete=models.CASCADE)

    authors = models.ManyToManyField(to=Author)

    def __str__(self):
        return self.name
