from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=200,default=None)
    details = models.TextField()
    date_created = models.DateTimeField()


    def __str__(self) -> str:
        return self.title+self.details