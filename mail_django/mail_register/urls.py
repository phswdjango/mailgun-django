from django.urls import include, path
from mail_django.mail_register import views
app_name = 'mail_register'
urlpatterns = [
    path('', views.mail, name='mail')
]