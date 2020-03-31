from django.shortcuts import render
from blog.models import Contact
from django.core.mail import send_mail
from texttutils.settings import EMAIL_HOST_USER
import requests
from bs4 import BeautifulSoup

# Create your views here.

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        desc = request.POST.get('desc','')
        print('name=',name)
        print('email=',email)

        contact = Contact(name=name,email=email,desc=desc)
        contact.save()
     
        send_mail(name,desc,email,['bhoyasnehal08@gmail.com'],fail_silently=False)


        #thank = True
        return render(request,'contact.html') 

    return render(request,"contact.html")
