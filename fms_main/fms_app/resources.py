from import_export import resources
from .models import Student


class PostResource(resources.ModelResource):
    class Meta:
        model = Student
