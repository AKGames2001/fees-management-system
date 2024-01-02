from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=6, choices=(("male", "Male"), ("female", "Female")))
    category_name = models.CharField(max_length=10)
    seat_type = models.CharField(max_length=10)
    fees_allotted = models.IntegerField(null=True)
    fees_paid = models.IntegerField(null=True)
    payment_status = models.CharField(max_length=10, choices=(("paid", "Paid"), ("pending", "Pending")), null=True)

    class Meta:
        ordering = ('student_id',)

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"


class FileUpload(models.Model):
    file = models.FileField(upload_to='pictures')
