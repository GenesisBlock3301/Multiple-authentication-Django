from django.contrib import admin
from .models import  Lecturar
from authentication.models import Student, User,CourseALlocation

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Lecturar)

class AllocattionAdmin(admin.ModelAdmin):
    list_display = ['lecturer']
admin.site.register(CourseALlocation,AllocattionAdmin)