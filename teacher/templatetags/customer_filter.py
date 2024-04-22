from django import template
register = template.Library() #这个实例必须命名为register

def to_sex(value,arg='zh'):
    change = {
        'zh':('女','男'),
        'en':('female','male')
    }
    return change[arg][value]

register.filter('to_sex',to_sex)

