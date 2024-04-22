from django.template import Library
register = Library()

@register.inclusion_tag('crm/paginator.html',takes_context=True)
def paginator_html(context):
    total_page=context['total_page']
    page = context['page']
    page_list = []
    num = 1

    #布置左边的页码
    if page - num <=0: #当前页左边不够显示，当前页就是
        for i in range(1,page+1):
            page_list.append(i)
    else:
        for i in range(page-num,page+1):
            page_list.append(i)

    #布置右边页码
    if page +num>=total_page:
        for i in range(page+1,total_page+1):
            page_list.append(i)
    else:
        for i in range(page+1,page+num+1):
            page_list.append(i)

    return {
        'page':page,
        'page_list':page_list,
    }

