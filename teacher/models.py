from django.db import models

# Create your models here.
class Student(models.Model): #Student模型是django.db.models.Model的子类
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField(null=True)
    sex = models.SmallIntegerField(default=1)
    qq = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=20,null=True)
    c_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    #detail = models.OneToOneField('StudentDetail',on_delete=models.SET_NULL,null=True)
    classroom = models.ForeignKey('classroom',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return '%s-%s'%(self.name,self.age)

class StudentDetail(models.Model):
    college = models.CharField(max_length=20,default='')
    student = models.OneToOneField('Student', on_delete=models.CASCADE)

    def __str__(self):
        return '%s'%self.college

class classroom(models.Model):
    name = models.CharField('班级名称', max_length=20)
    num = models.CharField('班期', max_length=20)

    def __str__(self):
        return '%s-%s'%(self.name,self.num)

class course(models.Model):
    name = models.CharField('课程名称',max_length=20)
    students = models.ManyToManyField('Student',through='Enroll')

    def __str__(self):
        return '%s'%self.name

class Enroll(models.Model):
    student = models.ForeignKey('Student',on_delete=models.CASCADE,null=True)
    course = models.ForeignKey('course',on_delete=models.CASCADE,null=True)
    c_time = models.DateTimeField('报名时间',auto_now_add=True)
