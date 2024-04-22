from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.shortcuts import redirect
from django.template.loader import get_template
from datetime import datetime
# Create your views here.

#def index(requset):
#    return HttpResponse('这是teacher下得index')

def login(request):
    return redirect('teacher:index')

def index(request):
    t = get_template('teacher/index.html')
    html = t.render()
    return HttpResponse(html)
#or render(request,'teacher/index.html')

def fuck(request):
    t = get_template('第一个.html')
    html = t.render()
    return HttpResponse(html)

def time(request):
    now =datetime.now()
    lt = [1,2,3]
    dt = {'name':'dean','age':38}
    student = [{'name':'dean','age':38},
               {'name': 'john', 'age': 28},
               {'name': 'alex', 'age': 18},
               {'name': 'david', 'age': 28}

    ]
    return render(request,'teacher/index.html',context={
        'now':now,
        'lt':lt,
        'dt':dt,
        'student':student,
    })

def login_v3(request):
    return render(request,'teacher/login-v3.html')

def login_v2(request):
    return render(request,'teacher/login-v2.html')

def detail(request,name):
    return HttpResponse('学生详情%s'%name)