from django.db import models

# Create your models here.
class Student(models.Model):
    s_username=models.CharField(max_length=100, primary_key=True)
    s_name=models.CharField(max_length=100)
    s_mobile=models.IntegerField()
    s_email=models.EmailField()
    s_password=models.IntegerField()
    def __str__(self):
        return self.s_username