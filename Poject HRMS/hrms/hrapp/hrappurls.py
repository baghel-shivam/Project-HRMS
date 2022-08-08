from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('saveenq/',views.savenq, name='saveenq'),
    path('registerdata/',views.registerdata, name='registerdata'),
    path('adminlogin/',views.user, name='adminlogin'),
]