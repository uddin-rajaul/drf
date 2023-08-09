from django.urls import path
from core.views import  TestAPI, CheckListAPIView

urlpatterns = [
    path('',TestAPI.as_view()),
    path('api/checklist/', CheckListAPIView.as_view())
]
