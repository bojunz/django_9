from django import  template
register = template.Library()

@register.filter
def to_male(value,arg):
    change ={
        'zh':('女','男'),
        'en':('female','male')
    }
    return change[arg][value]