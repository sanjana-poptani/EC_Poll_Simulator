from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('add_candidates/',add_candidates,name='add_candidates'),
    path('add_candidates/<str:alert>/',add_candidates,name='candidates'),
    path('poll/',poll,name='poll'),
    path('poll/<str:alert>',poll,name='poll1'),
    path('Summary/',votingSummary,name='summary'),
    path('pollResult/',pollResult,name='result')
]
