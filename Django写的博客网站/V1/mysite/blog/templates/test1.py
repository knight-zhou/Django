#coding:utf8
from django.db import models
from django.contrib import admin

# Create your models here.
#获取tittle ，body和时间

class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()

body = models.TextField()
print body