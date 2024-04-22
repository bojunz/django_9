from datetime import datetime
from django.template import Library

register = Library()



def current_time(x):
    return datetime.now().strftime(x)

register.simple_tag(current_time,name='current')

@register.inclusion_tag('teacher/show list.html')
def show_list(value,style='link'):
    return {'ls':value,'style':style}
