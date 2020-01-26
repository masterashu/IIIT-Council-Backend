from django.urls import path
from ..view.collaboration import *

urlpatterns = [
  path('MoU', collab_MoU_view, name='collab_MoU'),
  path('student_exchange', collab_student_exchange_view, name='collab_student_exchange'),
]
