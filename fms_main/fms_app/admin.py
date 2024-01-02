from django.contrib import admin
from .models import Post, FileUpload
from import_export.admin import ImportExportModelAdmin


# Register your models here.

# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('student_id', 'first_name', 'last_name')

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


# admin.site.register(Post)
