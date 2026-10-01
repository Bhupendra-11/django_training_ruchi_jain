from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from student.models import Student
from django.urls import reverse
from django.template import loader
import joblib


def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')

def stud(request):
    s=Student()
    u=Student.objects.filter(s_username=request.POST['s_username'])
    if not u:
        s.s_username=request.POST['s_username']
        s.s_password=request.POST['s_password']
        s.s_name=request.POST['s_name']
        s.s_mobile=request.POST['s_mobile']
        s.s_email=request.POST['s_email']
        s.save()
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'signup.html', {'errormsg':'Username already exist!'})

def login(request):
    return render(request, 'spp.html')


def login_valid(request):
    try:
        Student1=Student.objects.get(
            s_username=request.POST['s_username'],
            s_password=request.POST['s_password']
        )
        return HttpResponseRedirect(reverse('home'))
    except Student1.DoesNotExist:
        return render(request, 'login.html', {'erg':'Invalid Username or Password!'})    
    

def result(request):
    scaler=joblib.load('scaler_model.pkl')
    mlmodel=joblib.load('ml_model.pkl')
    lis=[]
    lis.append(request.GET['cgpa'])
    lis.append(request.GET['iq'])
    lis.append(request.GET['profile_score'])
    scale_input=scaler.transform([lis])
    ans=mlmodel.predict(scale_input)[0]
    res = render(request, 'result.html', {'ans':ans, 'lis':lis})
    return res
