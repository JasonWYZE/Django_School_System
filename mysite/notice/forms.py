from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class addNoticeform(ModelForm):
    class Meta:
        model=Notice
        fields="__all__"