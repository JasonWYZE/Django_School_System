from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework import viewsets


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return self.request.user.student.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)