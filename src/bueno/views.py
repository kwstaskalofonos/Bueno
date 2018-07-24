from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
	context={
	 "title":"Καλώς ήρθατε στο Bueno Crepa"
	}
	return render(request, "home_page.html", context)

def contact_page(request):

	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			subject = contact_form.cleaned_data['subject']
			email = contact_form.cleaned_data["email"]
			content = contact_form.cleaned_data["content"]
			from_email = email
			to_email = [settings.EMAIL_HOST_USER]
			contact_message="%s: %s via %s"%(
				subject, 
				content,
				email)
			contact_form = ContactForm(request.POST or None)
			send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
			return redirect("contact_page.html")
	else:
		contact_form = ContactForm()		
		context={
			"title":"Επικοινωνία",
			"form":contact_form
		}
	return render(request, "contact_page.html", context)

def login_page(request):
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			logusername = login_form.cleaned_data["username"]
			logpassword = login_form.cleaned_data["password"]
			user = authenticate(request, username=logusername, password=logpassword)
			print(user)
			if user is not None:
				login(request,user)
				return redirect(home_page)
			else:
				login_form = LoginForm()
				context={
					"title":"Είσοδος",
					"form":login_form
				}
				return redirect("/login")
	else:
		login_form = LoginForm()
		context={
			"title":"Είσοδος",
			"form":login_form
		}
	return render(request, "auth/login_page.html", context)

User = get_user_model()
def register_page(request):
	if request.method == 'POST':
		register_form = RegisterForm(request.POST)
		context={
			"title":"Εγγραφή",
			"form": register_form
		}
		if register_form.is_valid():
			regusername = register_form.cleaned_data["username"]
			regemail = register_form.cleaned_data["email"]
			regpassword = register_form.cleaned_data["password"]
			new_user = User.objects.create_user(regusername, regemail, regpassword)
			return redirect(home_page)
	else:
		register_form = RegisterForm()
		context={
			"title":"Εγγραφή",
			"form": register_form
		}
	return render(request,"auth/register_page.html",context)

	
	