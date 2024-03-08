from django.urls import path
from main_page import views

app_name = 'main_page'

urlpatterns = [
    path('', view=views.index, name='index'),
]
