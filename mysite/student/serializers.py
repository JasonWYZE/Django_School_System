from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    major = serializers.ChoiceField(choices=Student.MAJOR_CHOICES)
    
    class Meta:
        model = Student
        fields = ('id', 'user', 'name', 'major')