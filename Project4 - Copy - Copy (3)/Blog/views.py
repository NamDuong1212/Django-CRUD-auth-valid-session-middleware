from django.shortcuts import render, redirect
from .forms import BlogForm, CreateUserForm
from .models import Blog
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
    
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                request.session['user_id'] = user.id
                messages.success(request, 'Account was create for ' + user.username)
            
                return redirect('login')
    
        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
    
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request,' username OR password is incorrect' )
            
        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('login')

# Search
@login_required(login_url = 'login')
def retrieve_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'search.html', {'blogs':blogs})               
        
# Update
def update_blog(request, pk):
    blogs = Blog.objects.get(id=pk)
    form = BlogForm(instance = blogs)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance = blogs)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {
        'blogs': blogs,
        'form': form,
    }
    return render (request,'update.html', context)

# Delete
def delete_blog(request, pk):
    blogs = Blog.objects.get(id= pk)
    if request.method == 'POST':
        blogs.delete()
        return redirect('/')
    
    context = {
        'blogs':blogs,
    }
    return render(request, 'delete.html', context)

def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = BlogForm()
    return render(request, 'add.html',{'form':form})