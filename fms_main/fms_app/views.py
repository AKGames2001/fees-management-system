from django.shortcuts import render
from .models import Post
from .resources import PostResource
from django.http import HttpResponse
from tablib import Dataset
import pandas as pd


# Create your views here.

def home(request):
    # all_posts = Post.objects.all()
    #
    # return render(request, 'index.html', {'all_posts': all_posts})


    # if request.method == 'POST':
    #     file = request.FILES['myFile']
    #     csv = pd.read_csv(file)
    #     print(csv.head)
    #     arr = csv['sum']
    #     total = sum(arr)
    #     return render(request, 'index.html', {'something': True, 'sum': total})
    # else:
    #     return render(request, 'index.html')

    if request.method == 'POST':
        person_resource = PostResource()
        dataset = Dataset()
        new_person = request.FILES['myFile']

        if not new_person.name.endswith('.xlsx'):
            print("Error: Wrong file extension")
            return render(request, 'index.html')

        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in imported_data:
            value = Post(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
            )
            value.save()
    return render(request, 'index.html')


def upload(request):
    return render(request, 'upload.html')
