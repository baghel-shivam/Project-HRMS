from pdb import post_mortem
#from black import re
from django.shortcuts import redirect, render ,reverse
#from numpy import double
from .models import Enquiry, Registration , AdminLogin
import datetime 
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def index(request):
    return render(request, "main.html")


def aboutus(request):
    return render(request, "aboutus.html")


def contact(request):
    return render(request, "contact.html")


def login(request):
    return render(request, "login.html")


def registration(request):

    return render(request, "registration.html")


def savenq(request):
    name = request.POST['Name']
    gender = request.POST['gender']
    address = request.POST['address']
    phnnum = request.POST['contactno']
    email = request.POST['email']
    enq = Enquiry(name=name, gender=gender, address=address,phn_num=phnnum, email=email)
    enq.save()

    return redirect(contact)


def registerdata(request):
    name = request.POST['Name']
    gender = request.POST['gender']
    address = request.POST['address']
    phnnum = request.POST['contactno']
    email = request.POST['email']
    qualification = request.POST['qulification']
    experience = request.POST['exp']
    #skill = request.POST['keyskill']
    dob = request.POST['dob']
    aadharnum = request.POST['aadhaar']
    regdate = datetime.date.today()

    registernew = Registration(name=name, gender=gender, address=address, phnnum=phnnum, email=email, qualification=qualification, experience=experience, dob=dob, adhaarnum=aadharnum, regdate=regdate)
    registernew.save()
    return redirect(registration)

def user(request):
    userId = request.POST['userId']
    password = request.POST['pass']
    msg = ''
    try:
        obj = AdminLogin.objects.get(userId = userId , password = password)
        if obj is not None:
            #request.sessioon['userId']=userId
            return redirect(reverse('adminzone:adminhome'))
    except ObjectDoesNotExist:
        msg = 'Invalid User'
    


    return render(request,"login.html",{'msg':msg})
