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

        if len(student_id) != 9 and not student_id.isnumeric():
            return render(request, 'login.html', {
                'error': 'wrong username or password',
                'type': 'student',
                'url': '/login_student/'
            })

        student = Student.objects.filter(student_id=student_id).values()

        if student:
            if student[0]['password'] == password:
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


def register_student(request):
    if request.method == "POST":
        student_id = request.POST['user']
        password = request.POST['password']
        conf_pass = request.POST['conf_pass']

        if len(student_id) != 9 and not student_id.isnumeric():
            return render(request, 'login.html', {
                'error': 'Student ID should be 9 characters',
                'type': 'student',
                'url': '/register_student/'
            })

        student = Student.objects.filter(student_id=student_id).values()

        if not student:
            if password == conf_pass:
                # request.session['student_id'] = student.student_id
                value = Student(
                    student_id=student_id,
                    password=password
                )
                value.save()

                query_string = urlencode({'student_id': student_id})
                url = '/u/student/?{}'.format(query_string)
                return redirect(url)
            return render(request, 'register.html', {
                'error': 'Password & Confirm Password mismatch',
                'type': 'student',
                'url': '/register_student/'
            })
        return render(request, 'login.html', {
            'error': 'User already exists',
            'type': 'student',
            'url': '/login_student/'
        })
    return render(request, 'register.html', {'type': 'student'})


def login_admin(request):
    if request.method == "POST":
        email = request.POST['user']
        password = request.POST['password']

        admin = Admin.objects.filter(email=email).values()

        if admin:
            if admin[0]['password'] == password:
                # request.session['student_id'] = student.student_id
                return redirect('/u/admin/')
        return render(request, 'login.html', {
            'error': 'Wrong username or password',
            'type': 'admin',
            'url': '/login_admin/'
        })
    return render(request, 'login.html', {'type': 'admin'})


def register_admin(request):
    if request.method == "POST":
        email = request.POST['user']
        password = request.POST['password']
        conf_pass = request.POST['conf_pass']

        admin = Admin.objects.filter(email=email).values()

        if not admin:
            if password == conf_pass:
                # request.session['student_id'] = student.student_id
                value = Admin(
                    email=email,
                    password=password
                )
                value.save()
                return redirect('/u/admin/')
            return render(request, 'register.html', {
                'error': 'Password & Confirm Password mismatch',
                'type': 'admin',
                'url': '/register_admin/'
            })
        return render(request, 'login.html', {
            'error': 'User already exists',
            'type': 'admin',
            'url': '/login_admin/'
        })
    return render(request, 'register.html', {'type': 'admin'})
