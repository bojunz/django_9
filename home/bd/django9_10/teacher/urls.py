from django.urls import path
from . import views
app_name = 'teacher'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('login/',views.login_v3,name='login'),
    path('fuck/',views.fuck),
    path('time/',views.time),
    path('login2/',views.login_v2),
    path('detail/<name>/',views.detail,name='detail')
]