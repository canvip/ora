from django import forms
from .models import SignUp
from django.forms import ModelForm


class SignUpForm(forms.ModelForm):
	class Meta:
		model=SignUp
		fields = ['firset_name']
		#fields = '__all__'
		



