from django.urls import path
from kafedra import views

app_name = 'kafedra_page'

urlpatterns = [
    path(route='auth_kafedra/', view=views.auth, name='auth_kafedra'),
    path(route='profile_kafedra/', view=views.profile, name='profile_kafedra')
]
