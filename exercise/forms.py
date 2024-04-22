from django import forms
from CRM.models import Student,StudentDetail

class Registerform(forms.Form):
    username = forms.CharField(label='用户名',max_length=20) #label与input标签中的name属性相同
    password = forms.CharField(label='密码',
                               max_length=9,
                               min_length=6,
                               widget=forms.PasswordInput(attrs={'placeholder':'请输入长度为6-8位的密码'}),
                               error_messages={'min_length':'密码长度小于6位',
                                               'max_length':'密码长度大于9位'})
    password_repeat = forms.CharField(label='再次输入密码',widget=forms.PasswordInput())
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean() #继承父类方法,保证父类所有的默认校验都可以正常执行

        #错误信息提示
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password != password_repeat:
            msg = '密码不一致'
            self.add_error('password_repeat',msg) #第一个参数放在某个字段，第二个参数是报错信息

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student  #指定模型
        exclude = ['is_delete']  #is_delete在前台是不需要显示的

class  StudentDetailForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        exclude = ['student']  #一对一关系不需要显示