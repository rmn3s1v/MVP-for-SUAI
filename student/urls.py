from django.urls import path
from student import views

app_name = 'student_page'

urlpatterns = [
    path(route='auth_student/', view=views.auth, name='auth'),
    path(route='profile/', view=views.profile, name='profile')
]
