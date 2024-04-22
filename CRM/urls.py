from django.urls import path
from . import views
app_name = 'CRM'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('delete/<pk>/',views.student_delete,name = 'delete'),
    path('detail/<pk>/',views.student_detail,name = 'detail'),
    path('add/',views.student_add, name='add'),
    path('edit/<pk>/',views.student_edit, name='edit'),





]