from django.urls import path
from mail_django.base import views
app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
]
