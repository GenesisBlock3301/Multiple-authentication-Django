from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StudentAddForm,LecturerAddForm
from .decorators import student_required,lecturer_required

def home(request):
    return render(request,'templates/home.html')

def StudentSignUp(request):
    if request.method == "POST":
        form = StudentAddForm(request.POST or None)
        if form.is_valid():
            student = form.save(commit=False)
            student.user_type = 'student'
            student.save()
            return redirect('home')
    else:
       form = StudentAddForm()
    return render(request,'Student_signup.html',{'form':form})

def LecturerSignUp(request):
    if request.method == "POST":
        form = LecturerAddForm(request.POST or None)
        if form.is_valid():
            lecturer = form.save(commit=False)
            lecturer.user_type = 'lecturer'
            lecturer.save()
            return redirect('home')
    else:
       form = LecturerAddForm()
    return render(request,'Student_signup.html',{'form':form})


def SignInView(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #print(username)
        #print(password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Error wrong username/password")
    return render(request, 'login_form.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
@student_required()
def ForStudent(request):
    print(request.user.is_student)
    # if request.user.is_authenticated:
    #     if request.user.is_student:
    #         return render(request,'student.html')
    #     else:
    #         return HttpResponse("Sorry")
    return render(request, 'student.html')

@login_required
@lecturer_required
def ForLecturer(request):
    # print(request.user.is_lecturer)
    # if request.user.is_authenticated:
    #     if request.user.is_lecturer:
    #         return render(request,'teacher.html')
    #     else:
    #         return HttpResponse("Sorry")
    return render(request, 'teacher.html')