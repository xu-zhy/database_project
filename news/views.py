from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib import messages

'''用户注册'''
def register(request):
    return_code = 0
    if request.method == 'POST':
        username = request.POST.get('username') # 要求用户名唯一
        passward = request.POST.get('password')
        
        try:
            user = User.objects.create_user(username=username, password=passward)
            user.save()
            if user:    # 注册成功后跳转至登录
                auth.login(request, user)
                return redirect('login')    
        except IntegrityError:
            return_code = 1           # 用户名已存在
            return render(request, 'register.html', {'return_code':return_code})
            
    return render(request, 'register.html', {'return_code':return_code})

'''用户登录'''
def login(request):   
    return_code = 0 
    if request.method == 'POST':        
        username = request.POST.get('username')        
        password = request.POST.get('password')        
          
        try:   
            user = auth.authenticate(username=username, password=password)   
            if user:            
                auth.login(request, user)   # 登录    
                return redirect('index')    # 登录成功后跳转至主页
            else:
                raise auth.models.PermissionDenied
        except auth.models.PermissionDenied:
            return_code = 1
            return render(request, 'login.html', {'return_code':return_code})
    return render(request, "login.html", {'return_code':return_code})

'''主页'''
def index(request):    
    name = request.user.username    
    password = request.user.password    
    return render(request, 'index.html', {'name':name})
