from django.shortcuts import render,redirect,reverse
from exercise.forms import Registerform
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

# Create your views here.

def index(request):
    name =request.session.get('name','游客')
    return render(request,'exercise/index.html',context={
        'name' :name,
        'dog':'xixi'
    })

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        if username =='qwe' and password =='qwe':
            request.session['name'] = username
            request.session.set_expiry(10)
            return redirect('exercise:index')

    return render(request,'exercise/login.html')

def logout(request):
    request.session.flush()
    return redirect('exercise:index')

def register(request):
    if request.method =='GET':
        form = Registerform()
    # return render(request,'exercise/register.html',context={
    #     'form':form
    # })
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            email = form.cleaned_data.get('email')
            if password_repeat ==password:
                return HttpResponse('注册成功')
    return render(request,'exercise/register.html',context={
        'form':form,
        'test':'test'
    })



def article(request):
    return redirect(reverse('exercise:article_new'))

def article_new(request):
    return HttpResponse('这是新的网站首页')

