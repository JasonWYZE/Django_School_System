from django.db import models

# Create your models here.
class Notice(models.Model):
    Message = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField()


    def __str__(self) -> str:
        return self.Message