from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.models import User as U

from django.db import transaction

from authentication.models import Student,Lecturar


class LecturerAddForm(UserCreationForm):
    address = forms.CharField(max_length=30,widget=forms.TextInput(),label="Address")
    phone = forms.CharField(max_length=30, widget=forms.TextInput(),label='Mobile No')
    firstname = forms.CharField(max_length=30,widget=forms.TextInput(),label="Firstname")
    lastname = forms.CharField(max_length=30, widget=forms.TextInput(), label="Lastname")
    email = forms.CharField(max_length=30, widget=forms.TextInput(), label="Email")

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_lecturer = True
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        # if commit:
        #     user.save()
        # return user
        lecturer = Lecturar.objects.create(user=user, id_number=user.username)
        lecturer.save()
        return lecturer

class StudentAddForm(UserCreationForm):
    username = forms.CharField(max_length=30,widget=forms.TextInput(),label='Username')
    Address = forms.CharField(max_length=30, widget=forms.TextInput(), label='Address')
    phone = forms.CharField(max_length=30, widget=forms.TextInput(), label='Mobile No')
    firstname = forms.CharField(max_length=30, widget=forms.TextInput(), label="Firstname")
    lastname = forms.CharField(max_length=30, widget=forms.TextInput(), label="Lastname")
    email = forms.CharField(max_length=30, widget=forms.TextInput(), label="Email")

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        student = Student.objects.create(user=user,id_number=user.username)
        student.save()
        return student

