from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    completed = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.title+self.details