from django.shortcuts import redirect,render
from rest_framework import viewsets
from .serializers import noticeSerializer
from .models import Notice

# Create your views here.
class noticeView(viewsets.ModelViewSet):
    serializer_class = noticeSerializer
    queryset = Notice.objects.all()