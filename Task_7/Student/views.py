from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from Student.models import user
from Student.models import student
from django.urls import reverse


def home(request):
    return render(request, 'home.html')

def newStudentForm(request):
    return render(request, 'newStudentForm.html')

def signup(request): 
    return render(request, 'signup.html') 

def login(request):
    return render(request, 'login.html')

def login_valid(request):
    try:
        user1=user.objects.get(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return HttpResponseRedirect(reverse('newStudentForm'))
    except user.DoesNotExist:
        return render(request, 'login.html', {'erg':'Invalid Username or Password!'})    

def saveuser(request):
    user1=user()
    u=user.objects.filter(username=request.POST['username'])
    if not u:
        user1.username=request.POST['username']
        user1.password=request.POST['password']
        user1.name=request.POST['name']
        user1.save()
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'signup.html', {'errormsg':'Username already exist!'})
             

def saveStudent(request):
    s_id = request.POST['s_id']
    s_name = request.POST['s_name']
    s_branch = request.POST['s_branch']
    stu = student(s_id=s_id, s_name=s_name, s_branch=s_branch)
    stu.save()
    url=reverse('studentlist')
    return HttpResponseRedirect(url)


def studentlist(request):         # read Records (R of CRUD)
    Students = student.objects.all()
    res = render(request, 'studentlist.html', {'Students':Students})
    return res
