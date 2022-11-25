from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from . models import Person

# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('apply')
        else:
            messages.info(request,"please register")
            return redirect('register')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)

                user.save();
                return redirect('login')


        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')


    return render(request,"register.html")

def apply(request):
    return render(request,"apply.html")
def form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        phonenumber=request.POST.get('phonenumber')
        person=Person(name=name,address=address,phonenumber=phonenumber)
        person.save()
        return redirect('/credentials/info')
    return render(request,"form.html")
def info(request):
    task1 = Person.objects.all()
    return render(request,"info.html",{'task1':task1})