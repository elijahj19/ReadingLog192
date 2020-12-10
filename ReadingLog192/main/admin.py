from django.contrib import admin
from main.models import Course, Paper, User

# Register your models here.
admin.site.register(Course)
admin.site.register(Paper)
admin.site.register(User)