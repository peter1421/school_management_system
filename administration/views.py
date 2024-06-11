from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import FileResponse
import os
from teacher.models import Department, Designation
from .forms import *

def admin_login(request):
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {'forms': forms}
    return render(request, 'administration/login.html', context)

def admin_logout(request):
    logout(request)
    return redirect('login')


def add_designation(request):
    forms = AddDesignationForm()
    if request.method == 'POST':
        forms = AddDesignationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('designation')
    designation = Designation.objects.all()
    context = {'forms': forms, 'designation': designation}
    return render(request, 'administration/designation.html', context)



def db_download(request):
    # 指定你的 SQLite 數據庫文件的路徑
    db_path = 'db.sqlite3'

    # 確保文件存在
    if os.path.exists(db_path):
        # 返回文件響應，讓用戶可以下載
        return FileResponse(open(db_path, 'rb'), as_attachment=True, filename='db.sqlite')
    else:
        # 如果文件不存在，可以返回一個錯誤響應
        from django.http import HttpResponseNotFound
        return HttpResponseNotFound('The requested db file is not available')
