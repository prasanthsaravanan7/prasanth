from django.contrib import admin

# Register your models here.
from.models import Category, Questions, Student


admin.site.register(Category)
admin.site.register(Questions)
admin.site.register(Student)
