from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Users
from .forms import ContactForm
# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    contactform = ContactForm(request.POST or None)
    pub_date = timezone.now()
    if contactform.is_valid():
        data = contactform.cleaned_data
        db_register = Users(
            fullname = data.get("fullname"),
            email = data.get("email"),
            message = data.get("message"),
            pub_date = pub_date )
        db_register.save()
        
    return render(request, 'blog/contact.html', {'form':contactform})