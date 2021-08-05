from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import info
def home(request):
    return render(request,'sriapp/home.html')
def login(request):
    if request.method == "POST":
        password = request.POST['password']
        username = request.POST["username"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, "sriapp/index.html")
        else:
            return render(request, "sriapp/login.html")
    else:
        return render(request, "sriapp/login.html")
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        email = request.POST['email']
        p_number = request.POST['p_number']

        password = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST["username"]
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return render(request, "sriapp/register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return render(request, "sriapp/register.html")
            else:
                user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name, last_name=last_name)
                ins = info(email=email, Firstname=first_name, Lastname=last_name,ph_number=p_number)
                user.save();
                ins.save()

                messages.info(request,"sucuessfully registered")
                return render(request, "sriapp/register.html")
    else:
        return render(request, "sriapp/register.html")

# Create your views here.
