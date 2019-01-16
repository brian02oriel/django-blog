from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.urls import reverse

from .models import Users
from .forms import ContactForm
# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def home(request):
    
    #Selecciona los datos para mostrarlos en pantalla
    comments = Users.objects.all()
   
    #print(comments)
    return render(request, 'blog/home.html', {"data":comments})

def contact(request):
    #Inserta los datos del formulario en la db
    pub_date = timezone.now()
    contactform = ContactForm(request.POST)
    if request.method == 'POST':
        if contactform.is_valid():
            data = contactform.cleaned_data
            #print(data)
            db_register = Users(
                fullname = data.get("fullname"),
                email = data.get("email"),
                message = data.get("message"),
                pub_date = pub_date )
            db_register.save()
            return HttpResponseRedirect(reverse('blog:home'))
    else:
        return render(request, 'blog/contact.html', {'form':contactform})