from django.urls import path
from ..view.education import *

urlpatterns = [
    path('btech', education_btech, name='education_btech'),
]
