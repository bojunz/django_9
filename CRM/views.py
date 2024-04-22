from django.shortcuts import render
from CRM.models import Student,StudentDetail,classroom,course,Enroll
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import reverse
from django9_10.settings import MEDIA_ROOT
from django.template.loader import get_template
from django.core.paginator import Paginator
from exercise.forms import Registerform,StudentForm,StudentDetailForm

# Create your views here.
def home(request):
    search = request.GET.get('search', ' ').strip()
    if search:
        if search.isdigit():
            students = Student.objects.filter(Q(qq=search)|Q(phone=search))
        else:
            students = Student.objects.filter(name = search)
    else:
        students = Student.objects.all()
        students = students.order_by('c_time')
    #实现分页：只需要展示指定页面的数据信息
    total_num = students.count()
    page = request.GET.get('page',2)  #当前页码
    per_page = request.GET.get('per_page',3) #每页数据量

    paginator = Paginator(students,per_page,allow_empty_first_page=True)#实例化
    students = paginator.get_page(page) #当前页展示的数据

    # total_page = paginator.num_pages()



    return render(request,'crm/home.html',context={
        'students':students,
        'search':search,
        # 'total_page':total_page,
        'page':page,
    })

def student_delete(request,pk):
    student = Student.objects.get(pk=pk)
    student.is_delete = True
    student.save()
    return redirect(reverse('CRM:home'))

def student_detail(request,pk):
    section = ' 学生详情'
    student = Student.objects.get(pk=pk)
    grades = classroom.objects.all()
    return render(request,'crm/detail.html',context={
        'section':section,
        'grades':grades,
        'student':student
    })

def student_add(request):
    section = '添加学生信息'
    if request.method == 'GET':
        grades = classroom.objects.all()

        return render(request,'crm/detail.html',context={
            'section':section,
            'grades':grades})
    if request.method =='POST':
        #学生列表信息，更新学生表
        data = {
            'name':request.POST.get('name'),
            'age':request.POST.get('age'),
            'sex':request.POST.get('sex'),
            'qq':request.POST.get('qq'),
            'phone':request.POST.get('phone'),
            'grade.id':request.POST.get('classroom'),
        }
        student = Student.objects.create(**data)

        #获取学生详情并更新数据库
        StudentDetail.objects.create(
            num=request.POST.get('num'),
            college=request.POSt.get('college'),
            student = student
        )

        return redirect(reverse('CRM:home'))

# def studnent_edit(request,pk):
#     section = '修改学生信息'
#     student = Student.objects.get(pk=pk)
#     grades = classroom.objects.all()
#     if request.method=='GET':
#         return render(request,'crm/detail.html',context={
#             'section':section,
#             'student':student,
#             'grades':grades,
#         })
#     if request.method=='POST':
#         #学生列表的更新
#         grade_id = request.POST.get('grade')
#         try:
#             grades =classroom.objects.get(pk=grade_id)
#         except:
#             grades =None
#         student = Student.objects.get(pk=pk)
#         student.name = request.POST.get('name')
#         student.sex = request.POST.get('sex')
#         student.age = request.POST.get('age')
#         student.phone = request.POST.get('phone')
#         student.qq = request.POST.get('qq')
#         student.classroom = grades
#
#         #学生详情表更新
#         try:
#             student_detail =student.detail
#         except:
#             student_detail = StudentDetail()
#             student_detail.student = student
#         student_detail.num = request.POST.get('num')
#         student_detail.college= request.POST.get('college')
#
#         student_detail.save()
#         student.save()
#         return redirect(reverse('CRM:home'))

def student_edit(request,pk):
    section ='修改学生信息'
    student = Student.objects.get(pk=pk)

    form =StudentForm(instance=student)
    # try:
        # detail_form = StudentDetailForm(instance=student.detail)

    return render(request,'crm/detail_form.html',context={
        'section' :section,
    })
