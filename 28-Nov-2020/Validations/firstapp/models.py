from django.db import models

# Create your models here.
class Register(models.Model):

	vals = [('Male','Male'),('Female','Female')]
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=10)
	emailId = models.EmailField(null=True)
	phoneNo = models.CharField(max_length=10)
	age = models.IntegerField(null=True)
	gender= models.CharField(max_length=10,choices=vals)
	date_of_birth = models.DateField(null=True)

	def __str__(self):
		return self.emailId