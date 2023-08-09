from django.urls import path
from core.views import  TestAPI

urlpatterns = [
    path('',TestAPI.as_view()),

]
