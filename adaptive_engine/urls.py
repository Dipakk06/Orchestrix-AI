from django.urls import path
from . import views

app_name = 'adaptive_engine'

urlpatterns = [
    path('skill-tree/<int:course_id>/', views.skill_tree, name='skill_tree'),
]
