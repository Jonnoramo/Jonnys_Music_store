from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
	first_name = forms.CharField(label='First name')
	surname = forms.CharField(label='Surname')
	credit_card_number =forms.CharField(label='Credit Card Number')
	cvv = forms.CharField(label = '3 digit number')
	stripe_id = forms.CharField(widget=forms.HiddenInput)
	house_number = forms.CharField(label= 'House Number')
	street = forms.CharField(label= 'Street')
	city = forms.CharField(label= 'city')
	occupation = forms.CharField(label= 'Occupation')


	class Meta:
		model = User
		fields = ['email',  'password', 'stripe_id', 'first_name', 'surname', 'city', 'occupation']

	def clean_email(self):
		email = self.cleaned_data.get('email')

		if not email:
			message = "Please enter a valid email address"
			raise forms.ValidationError(message)

		return email
		
class UserLoginForm(forms.Form):
	email = forms.EmailField()	
	password = forms.CharField(widget=forms.PasswordInput)	