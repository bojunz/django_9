from django import template

register = template.Library() #生成一个注册器

#方法二 用装饰器，装饰器的方法名默认函数名
#默认自动调用下面的函数
@register.filter()
def my_upper(value):  #必须要带一个参数
    return value.upper()

#这是方法一 用register调用函数
register.filter(my_upper)  #函数体就是调用的名字

@register.filter()
def my_times(value,x):
    return value*x
#调用时 {{ num1|my_times:3}} 在函数名后面冒号加数字


#上面是过滤器
#下面是模板标签
import datetime

@register.simple_tag
def current_time():
    format_time = '%Y年%m月%d日 %H:%M:%S'
    return datetime.datetime.now().strftime(format_time)

@register.simple_tag
def current_time1(format_time):
    return datetime.datetime.now().strftime(format_time)

#从views context获取值时， 函数参数一定要为context
@register.simple_tag(takes_context=True)
def takes(context):
    ft = context.get('name')
    return ft


#包含标签,无参数
@register.inclusion_tag('exercise/show_tag.html')
def show_tags():
    li = ['香蕉','苹果','山竹','西瓜']
    return {'values':li}

#包含标签，有参数
@register.inclusion_tag('exercise/show_tag.html')
def show_tags1(li):
    return {'values':li}

@register.inclusion_tag('exercise/show_tag.html',takes_context=True)
def show_tags2(context):
    li = context.get('test')
    return {'values':li}



