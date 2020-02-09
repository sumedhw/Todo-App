from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=20)
    member = models.IntegerField(max_length=2000 , null=True)
    description = models.CharField(max_length=20 , null=True)
    date = models.DateTimeField( null = True)
    date_created = models.DateTimeField(auto_now_add=True , null = True)

    def __str__(self):
        return self.name