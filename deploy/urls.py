from django.urls import path
from .views import StudentListCreateApiVIew, StudentDetailApiView

urlpatterns = [
    path('students/', StudentListCreateApiVIew.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailApiView.as_view(), name='student-detail'),
]