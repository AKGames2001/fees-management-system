from django.db import models


# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField()
    password = models.CharField(max_length=20)


class Admin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)
