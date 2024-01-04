from django.shortcuts import render, redirect
from urllib.parse import urlencode
from .models import Student, Admin


# Create your views here.

def home(request):
    return render(request, 'home.html')


def login_student(request):
    if request.method == "POST":
        student_id = request.POST['user']
        password = request.POST['password']

        student = Student.objects.filter(student_id=student_id).values()[0]

        if student:
            if student['password'] == password:
                # request.session['student_id'] = student.student_id
                query_string = urlencode({'student_id': student_id})
                url = '/u/student/?{}'.format(query_string)
                return redirect(url)
        return render(request, 'login.html', {
            'error': 'Wrong username or password',
            'type': 'student',
            'url': '/login_student/'
        })
    return render(request, 'login.html', {'type': 'student'})


def login_admin(request):
    if request.method == "POST":
        email = request.POST['user']
        password = request.POST['password']

        admin = Admin.objects.filter(email=email).values()[0]

        if admin:
            if admin['password'] == password:
                # request.session['student_id'] = student.student_id
                return redirect('/u/admin/')
        return render(request, 'login.html', {
            'error': 'Wrong username or password',
            'type': 'admin',
            'url': '/login_admin/'
        })
    return render(request, 'login.html', {'type': 'admin'})
