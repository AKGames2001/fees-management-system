from django.db import models


class Student(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=6, choices=(("M", "Male"), ("F", "Female")))
    category_name = models.CharField(max_length=10)
    seat_type = models.CharField(max_length=10)
    fees_allotted = models.IntegerField(null=True)
    fees_paid = models.IntegerField(null=True)
    payment_status = models.CharField(max_length=10, choices=(("paid", "Paid"), ("pending", "Pending")), null=True)

    class Meta:
        ordering = ('student_id',)

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"


class Fee(models.Model):
    type_open = models.IntegerField()
    type_obc = models.IntegerField(null=True)
    type_obc_min = models.IntegerField(null=True)
    type_vj = models.IntegerField(null=True)
    type_vj_min = models.IntegerField(null=True)
    type_nt = models.IntegerField(null=True)
    type_nt_min = models.IntegerField(null=True)
    type_sbc = models.IntegerField(null=True)
    type_sbc_min = models.IntegerField(null=True)
    type_sc = models.IntegerField(null=True)
    type_st = models.IntegerField(null=True)
    type_pwd = models.IntegerField(null=True)
    type_rcsms = models.IntegerField(null=True)
    type_ews = models.IntegerField(null=True)
    type_sebc = models.IntegerField(null=True)
    type_tfws = models.IntegerField(null=True)
    type_jk = models.IntegerField(null=True)
    type_ne = models.IntegerField(null=True)
    type_pmsss = models.IntegerField(null=True)
    type_ciwg = models.IntegerField(null=True)


class Course(models.Model):
    course_name = models.CharField(max_length=10)
    fee_id = models.ForeignKey(Fee, on_delete=models.CASCADE)
