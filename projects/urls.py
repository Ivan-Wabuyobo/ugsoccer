from django.urls import path
from .views import *
urlpatterns = [
    path('', project_index, name='index'),
    path('<int:pk>/', project_detail, name='details')
]