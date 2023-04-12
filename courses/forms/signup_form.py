from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(UserCreationForm):
	first_name = forms.CharField(max_length=20, required=True)
	last_name = forms.CharField(max_length=20, required=True)
	email = forms.EmailField(required=True)
	username = forms.CharField(required=True, widget=False)

	class Meta:
		model = User
		fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

