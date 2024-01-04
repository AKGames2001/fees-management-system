from django.contrib import admin
from .models import Post
from import_export.admin import ImportExportModelAdmin


@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    list_display = (
        'student_id',
        'first_name',
        'last_name',
        'course_name',
        'branch_name',
        'email',
        'gender',
        'category_name',
        'seat_type',
        'fees_allotted',
        'fees_paid',
        'payment_status'
    )
