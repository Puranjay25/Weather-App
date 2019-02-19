#this file is not used
from django import forms
from .models import city

class cityform(forms.ModelForm):
	class Meta:
		model=city
		fields=['city_name']