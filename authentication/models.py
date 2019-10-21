from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    phone = models.CharField(max_length=60,blank=True, null=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id_number = models.CharField(max_length=255)

    def __str__(self):
        return self.id_number
    # def get_absolute_url(self):
    #     return reverse('profile')

class Lecturar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=255)

    def __str__(self):
        return self.id_number

    # def get_absolute_url(self):
    #     return reverse('profile')
class CourseALlocation(models.Model):
    lecturer = models.ForeignKey(User,on_delete=models.CASCADE)

