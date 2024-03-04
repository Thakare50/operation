from django.contrib import admin
from testapp.models import Student
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display=['sid','sname','sage','slocation']

admin.site.register(Student,studentAdmin)