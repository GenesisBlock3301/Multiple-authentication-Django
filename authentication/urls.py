from django.urls import path

from authentication import views

urlpatterns = [
    path('',views.home,name='home'),
    path('student/signup/',views.StudentSignUp, name = 'StudentSignup'),
    path('lecturar/signup/',views.LecturerSignUp, name = 'LecturerSignup'),
    path('login/',views.SignInView,name = 'login'),
    path('logout/',views.logout_view,name = 'logout'),
    path('forstudent/',views.ForStudent,name='forStudent'),
    path('forlecturer/',views.ForLecturer,name='forLecturer'),
]