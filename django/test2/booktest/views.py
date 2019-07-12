from django.shortcuts import render, redirect # 重定向
from booktest.models import BookInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    '''显示图书信息'''
    # 1。 查询所有图书的信息
    books = BookInfo.objects.all()
    # 2. 使用模板
    return render(request, 'booktest/index.html', {'books':books})

def create(request):
    '''新增书籍'''
    # 1. 创建BookInfo对象
    b = BookInfo()
    b.btitle = '流星蝴蝶剑2'
    b.bpub_date = date(1990,1,4)
    # 2. 保存数据库
    b.save()
    # 3.返回应答
    # return HttpResponse('ok') # 保存数据了,但是u跳转了
    # return HttpResponseRedirect('/index') # 重定向
    return redirect('/index') # 重定向内部重写HttpResponseRedirect

def delete(request, bid):
    '''删除点击的图书'''
    # 1. 通过bid获取图书对象
    book = BookInfo.objects.get(id=bid)
    # 2. 删除
    book.delete()
    # 3. 重定向
    return HttpResponseRedirect('/index')