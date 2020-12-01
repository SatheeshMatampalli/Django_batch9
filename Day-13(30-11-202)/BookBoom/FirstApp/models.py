from django.db import models

# Create your models here.
class Books(models.Model):
	BookName=models.CharField(max_length=50)
	BookId=models.IntegerField(null=True)
	BookAuthor=models.CharField(max_length=50)
	BookImage=models.ImageField(upload_to='bookimages/',null=True)