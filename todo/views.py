from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Tasks
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def complete_task(request,task_id):
    task = get_object_or_404(Tasks,id = task_id)
    task.status = True
    task.save()
    return redirect("/home")

@login_required
def delete_task(request,task_id):
    task = get_object_or_404(Tasks,id = task_id)
    task.delete()
    return redirect("/home")

def login(request):
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    return render(request,'register.html')

@login_required
def home(request):
    filter_by = request.GET.get('filter','all')
    if filter_by == 'active':
        tasks = Tasks.objects.filter(user = request.user, status = False)
    elif filter_by == 'completed':
        tasks = Tasks.objects.filter(user = request.user, status = True)
    else:
        tasks = Tasks.objects.filter(user = request.user)
    return render(request, 'home.html',{'tasks':tasks,'filter':filter_by})

def verifyregister(request):
    if request.method == 'POST':
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if password1 != password2:
            messages.info(request,'Password doesnot match')
            return redirect("/register")
        if User.objects.filter(username = username).exists():
            messages.info(request,'Username already taken')
            return redirect("/register")    
        if User.objects.filter(email = email).exists():
            messages.info(request,'Email already taken')
            return redirect("/register") 
        user = User.objects.create_user(
            first_name = firstname,
            last_name = lastname,
            email = email,
            password = password1,
            username = username
        )     
        user.save()
        return redirect('/')
    return redirect('/register')

def verifylogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username , password = password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('/')
    return redirect('/')

@login_required
def addtask(request):
    if request.method == "POST":
        task = request.POST['task']
        Tasks.objects.create(
            title = task,
            status = False,
            user = request.user,
        )
        
    return redirect('/home')


