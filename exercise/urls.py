from django.urls import path
from . import views
app_name = 'exercise'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name ='register'),
    path('article/',views.article),
    path('article_new/',views.article_new,name='article_new'),




]