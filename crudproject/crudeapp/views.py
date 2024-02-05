from django.shortcuts import render, redirect
from .models import user
from .forms import AddForm
from django.contrib.auth import logout
from django.contrib.auth.models import auth

# Create your views here.


def values(request):
    if request.method=='POST':
        Firstname = request.POST.get('firstname')
        Lastname = request.POST.get('lastname')
        Username = request.POST.get('username')
        Email = request.POST.get('email')    
        Password = request.POST.get('password')
        Age = request.POST.get('age')
        Phonenumber = request.POST.get('phonenumber')
        user(firstname=Firstname,lastname=Lastname,username=Username,email=Email,password=Password,age=Age,phonenumber=Phonenumber).save()
    return render(request,'user.html')


def view(request):
    cr = user.objects.all()
    return render(request,"view.html",{'cr':cr})

def detailview(request,pk):
    cr = user.objects.get(id=pk)
    return render(request,"detailview.html",{'cm':cr})


def update(request,pk):
    cr = user.objects.get(id=pk)
    form = AddForm(instance = cr)
    if request.method == "POST":
        form = AddForm(request.POST,instance = cr)
        if form.is_valid:
          form.save()
          return redirect("view")
    return render(request,"update.html",{'form':form})


def delete(request,pk):
    cr = user.objects.get(id=pk)
    cr.delete()
    return redirect('view')


def login(request):
    return render(request,"login.html")


def userlog(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        cr = user.objects.filter(username=username, password=password)

        if cr:
            login_details = user.objects.get(username=username,password=password)

            id=login_details.id
            username=login_details.username
            password=login_details.password

            request.session['id'] = id
            request.session['username'] = username
            request.session['password'] = password

            return redirect('welcome')
        else:
            return render(request,'login.html')
    else:
        return render(request,'view.html')
    
    
def welcome(request):
    id = request.session['id']
    username = request.session['username']
    return render(request,"welcomepage.html",{'id':id,'username':username})

def logoutuser(request):
    logout(request)
    return redirect('login')

def adminlog(request):
    return render(request,'adminlogin.html')

def alog(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('login')
        
        else:
            return redirect('adminlog')
        
    else:
        return render(request, 'adminlogin.html')