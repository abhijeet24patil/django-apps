from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
# Create your views here.
def home(request):
	title="welcome"
	# if request.user.is_authenticated():
	# 	title = "My Name is %s" %(request.user)
	# if request.method =="POST":
	# 	print request.POST

	form = SignUpForm(request.POST or None)
	context = {
	"title" : title,
	"form"  : form
	}
	
	if form.is_valid():
		# form.save()
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New Full name"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = "abhi" 
		instance.save()
		context = {
			"title" : "Thank you"
		}
	
	return render(request,"home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email,message,full_name
		subject='Site Contact Form'
		from_email= settings.EMAIL_HOST_USER
		to_email=[from_email,'abhijeet24patil@gmail.com']
		contact_message="%s %s via %s"%(
			form_full_name, 
			form_message, 
			form_email)
		
		some_html_message ="""
		<h1>Hello</h1>
		"""
		send_mail(subject, 
			contact_message, 
			from_email, to_email,
			html_message = some_html_message, 
			fail_silently=False)

	context={
		"form":form,
	}
	return render(request,"forms.html", context)
