from rest_framework import serializers
from .models import Notice

class noticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields=('id','title','details','date_created')
