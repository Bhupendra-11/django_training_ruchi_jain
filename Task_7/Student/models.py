from django.db import models

class user(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class student(models.Model):
    s_id = models.IntegerField()
    s_name = models.CharField(max_length=100)
    s_branch = models.CharField(max_length=100)  
    def __str__(self):
        return self.s_name  


# Create your models here.
