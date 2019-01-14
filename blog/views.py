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
    #Inserta los datos del formulario en la db
    pub_date = timezone.now()
    contactform = ContactForm(request.POST or None)
    if contactform.is_valid():
        data = contactform.cleaned_data
        print(data)
        db_register = Users(
            fullname = data.get("fullname"),
            email = data.get("email"),
            message = data.get("message"),
            pub_date = pub_date )
        db_register.save()
    
    #Selecciona los datos para mostrarlos en pantalla
    comments = Users.objects.all()
    for comment in comments:
        fullname = comment.fullname
        email = comment.email
        message = comment.message
        pub_date = comment.pub_date

    context = {
        "fullname":fullname,
        "email":email,
        "message":message,
        "pub_date":pub_date
    }
    return render(request, 'blog/home.html', context)

def contact(request):
    contactform = ContactForm(request.POST or None)
    
    return render(request, 'blog/contact.html', {'form':contactform})