from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    email=models.EmailField()
    text=models.TextField(max_length=100,default='',null=True,blank=True)


def __str__(self):
    return self.name
    