from django.db import models

# Create your models here.
class StudentData(models.Model):
	First_Name=models.CharField(max_length=50)
	Last_Name=models.CharField(max_length=50)
	College=models.CharField(max_length=50)
	Email=models.EmailField(max_length=50)
	Password=models.CharField(max_length=50)
	