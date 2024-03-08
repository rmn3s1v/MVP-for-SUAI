from django.urls import path
from partners import views

app_name = 'partners_page'

urlpatterns = [
    path(route='auth_partners/', view=views.auth, name='auth'),
    path(route='profile_part/', view=views.profile_part, name='profile_part')
]
