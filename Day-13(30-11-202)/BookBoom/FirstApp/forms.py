from django.forms import ModelForm
from FirstApp.models import Books

class BooksForm(ModelForm):
	class Meta:
		model = Books
		fields = '__all__'

