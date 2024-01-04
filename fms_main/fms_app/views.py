from django.shortcuts import render, redirect
from .models import Post, Course, Fee
from tablib import Dataset


# Create your views here.

def admin(request):
    studentData = Post.objects.all().values()
    return render(request, 'index.html', {"studentData": studentData})


def upload(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_person = request.FILES['myFile']

        if not new_person.name.endswith('.xlsx'):
            return render(request, 'upload.html', {'error': 'Wrong file extension'})

        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in imported_data:
            course_name = data[4].lower()
            category = 'type_' + data[8].lower()

            fee_id = Course.objects.filter(course_name=course_name).values()[0]
            fees_data = Fee.objects.filter(id=fee_id['fee_id_id']).values()[0]
            fees_allotted = int(fees_data[category])

            payment_done = fees_allotted - data[11]
            if payment_done == 0:
                payment_status = 'Paid'
            else:
                payment_status = 'Pending'

            value = Post(
                data[0],
                data[1],
                data[2],
                data[3],
                course_name,
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                fees_allotted,
                data[11],
                payment_status,
            )
            value.save()
        return redirect('/u/admin/')
    return render(request, 'upload.html')


def student(request, *args, **kwargs):
    std_id = request.GET.get('student_id')
    studentData = Post.objects.filter(student_id=std_id).values()
    return render(request, 'student_dashboard.html', {
        "studentData": studentData,
        'student_name': studentData[0]['first_name']
    })
