from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	subject = forms.CharField(
			widget=forms.TextInput(
				attrs={
					"class":"form-group form-control", 
					"placeholder":"email subject",
					})
			)
	email = forms.EmailField(
			widget=forms.EmailInput(
				attrs={
					"class":"form-group form-control", 
					"placeholder":"sender email",
					})
			)
	content = forms.CharField(
			widget=forms.Textarea(
				attrs={
					"class":"form-group form-control",
					"placeholder":"email content"
				})
			)
	def clean_subject(self):
		sub = self.cleaned_data.get("subject")
		if len(sub) < 6:
			raise forms.ValidationError("sub must be at least")
		return sub

class LoginForm(forms.Form):
	username = forms.CharField(
			widget=forms.TextInput(
				attrs={
					"class":"form-group form-control",
					"placeholder":"username"
				})
			)
	password = forms.CharField(
			min_length=8,
			widget=forms.PasswordInput(
				attrs={
					"class":"form-group form-control", 
					"placeholder":"password",
					})
			)

class RegisterForm(forms.Form):
	username = forms.CharField(
			widget=forms.TextInput(
				attrs={
					"class":"form-group form-control",
					"placeholder":"fill in the username"
				})
			)
	email = forms.EmailField(
			widget=forms.EmailInput(
				attrs={
					"class":"form-group form-control", 
					"placeholder":"fill in the email",
					})
			)
	password = forms.CharField(
			min_length=8,
			widget=forms.PasswordInput(
				attrs={
					"class":"form-group form-control", 
					"placeholder":"fill in the password",
					})
			)
	confirm_password = forms.CharField(
			min_length=8,
			widget=forms.PasswordInput(
				attrs={
					"class":"form-group form-control", 
					"placeholder":"fill in the password",
					})
			)

	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username is taken")
		return username

	def clean(self):
		data = self.cleaned_data
		pass1 = self.cleaned_data.get("password")
		pass2 = self.cleaned_data.get("confirm_password")
		if pass1 != pass2:
			raise forms.ValidationError("confirm password doesnt match the password")
		return data