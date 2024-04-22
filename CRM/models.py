from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    sex = models.SmallIntegerField(default=1)
    qq = models.CharField(max_length=20,unique=True)
    phone = models.CharField(max_length=20,unique=True)
    c_time = models.DateTimeField('创建时间',auto_now_add=True)
    e_time = models.DateTimeField('修改时间',auto_now=True)
    classroom = models.ForeignKey('classroom',on_delete=models.SET_NULL,null=True,related_name='student')
    is_delete = models.BooleanField(default='False')

    def __str__(self):
        return '%s%s' %(self.name,self.sex)

class StudentDetail(models.Model):
    num = models.CharField('身份证',max_length=40,default='',unique=True)
    college = models.CharField('毕业学校',max_length=20,default='')
    student = models.OneToOneField('Student',related_name='detail',on_delete=models.CASCADE)
    #relate_name 是给本表别名，当外表反向查询时，可以用别名加set

class classroom(models.Model):
    name = models.CharField('班级名字',max_length=20)
    num = models.CharField('班期',max_length=20)

    def __str__(self):
        return '%s'%self.name

class course(models.Model):
    name = models.CharField('课程名',max_length=20)
    student = models.ManyToManyField('Student',through='Enroll')

class Enroll(models.Model):
    student = models.ForeignKey('Student',on_delete=models.CASCADE)
    course = models.ForeignKey('course',on_delete=models.CASCADE)
    pay = models.FloatField('缴费金额',default=0)
    c_time = models.DateTimeField('报名时间',auto_now_add=True)