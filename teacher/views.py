from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
from django.shortcuts import redirect
from django.template.loader import get_template
from datetime import datetime
from teacher.models import Student
from django9_10.settings import MEDIA_ROOT
import os
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
    # t = get_template('第一个.html')
    # html = t.render()
    if request.method == 'GET':
        return render(request,'第一个.html')
    if request.method == 'POST':
        usr = request.POST.get('user')
        psw = request.POST.get('psw')
        if usr =='zxc' and psw=='123':
            return redirect('teacher:index')
        else:
            return render(request,'第一个.html')

def time(request):
    now =datetime.now()
    format_str = '%Y年%m月%d日 %H:%M:%S'
    lt = [1,2,3]
    dt = {'name':'dean','age':38}
    student = [{'name':'dean','age':38,'course':['python','java','C', 'english']},
               {'name': 'john', 'age': 28,'course':['python','java','C', 'english']},
               {'name': 'alex', 'age': 18,'course':['python','java','C', 'english']},
               {'name': 'david', 'age': 28,'course':['python','java','C', 'english']}]
    stus = Student.objects.all()


    return render(request,'teacher/index.html',context={
        'now':now,
        'lt':lt,
        'dt':dt,
        'student':student,
        'format_str':format_str,
        'stus':stus
    })

def login_v3(request):
    return render(request,'teacher/login-v3.html')

def login_v2(request):
    return render(request,'teacher/login-v2.html')

def detail(request,name):
    return HttpResponse('学生详情%s'%name)

def sub1(request):
    return render(request,'teacher/sub1.html')

def sub2(request):
    return render(request,'teacher/sub2.html')

def upload(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        #每天上传的文件放入每天的文件夹
        day_dir = datetime.now().strftime('%Y%m%d')
        day_url = os.path.join(MEDIA_ROOT,day_dir)
        if not os.path.exists(day_url):
            os.mkdir(day_url)
        #文件的写入
        #with open(文件保存路径，写入方式) as f:
        filename = os.path.join(day_url,file.name)
        with open(filename,'wb') as fb:
            for line in file.chunks():  #chunks函数自动把大文件分块
                fb.write(line)

        return HttpResponse('上传成功')

    return render(request, 'teacher/upload.html')

def cooike_test(request):
    num = request.COOKIES.get('num')
    if num:
        num = int(num) +1
    else:
        num =1
    response = render(request,'teacher/cookie.html',context={'num':num })

    # return render(request,'teacher/cookie.html',context={
    #     'num':num
    # })
    response.set_cookie('num',num,max_age=10)
    return response


