from django.urls import path
from . import views
urlpatterns = [
    path('adminzone/',views.adminhome,name='adminhome'),
]