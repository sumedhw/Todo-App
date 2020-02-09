from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth

from .models import Task

from django.contrib.auth.decorators import login_required

@login_required(login_url='/user_login')
def home(request):
    tasks = Task.objects.filter(member = request.user.id)

    context = { 'tasks' : tasks }

    return render(request , 'todoapp/home.html' , context)

def create_task(request):
    return render(request , 'todoapp/create_task.html')

def store_task(request):
    
    task = Task()
    task.name = request.POST.get('name')
    task.member = request.user.id
    task.description = request.POST.get('description')
    task.date = request.POST.get('date')
    task.save()
    messages.info(request , 'Created Successfully')
    return redirect("/")    

def delete_task(request, id):

    task = Task.objects.get(pk = id , member = request.user.id )  

    if task is None:
        messages.info(request , "Task not Found")
        return redirect("/")

    task.delete()   
    messages.info(request , "Task Deleted")
    return redirect("/")


def user_registration(request):
   if request.method == 'POST':
       first_name = request.POST.get('first_name')
       last_name = request.POST.get('last_name')
       user_name = request.POST.get('user_name')
       email = request.POST.get('email')
       mobile = request.POST.get('mobile')
       password1 = request.POST.get('password1') 
       password2 = request.POST.get('password2')

       if password1 == password2:
            if User.objects.filter(username = user_name).exists():
                messages.info(request, 'Username Taken')
                return redirect('todoapp:user_registration')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email Taken')
                return redirect('todoapp:user_registration')
            else:
                user = User.objects.create_user(first_name = first_name , last_name = last_name , username=user_name, email= email , password = password1)
                user.save()
                return redirect('todoapp:login')
       else:
            return redirect('todoapp:user_registration')
        
       return redirect('/')

   else:
        return render(request , 'todoapp/user_registration.html')

def login(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=user_name , password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request , 'Invalid credentials')
            return redirect('todoapp:login')
    else:
        return render(request , 'todoapp/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

    



