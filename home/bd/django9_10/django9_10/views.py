from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
def index(request):
    return HttpResponse('你好，这是大聪明项目')

def detail(request,id):
    return  HttpResponse(f'这是id是{id}的学生')

def student(request,year,month):
    return HttpResponse(f'这是{year}年{month}月的学生列表')

def register(request,arg):
    return HttpResponse('这是注册模块%s'%arg)

def student(request):
    return redirect('https://www.baidu.com')