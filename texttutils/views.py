# I have created this file -snehal

from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from .settings import EMAIL_HOST_USER
from django.views.decorators.csrf import csrf_exempt
import requests
from bs4 import BeautifulSoup

''' Read by Strings '''
# def index(request):
#     return HttpResponse("I am snehal")

# def contact(request):
#     # return HttpResponse(''' <h1>STARK INDUSTRIES PVT LTD</h1> <a href="https://www.youtube.com/?gl=IN">Snehal</a>  ''')

#     return HttpResponse('''
#     <ul>
#     <li><a href="https://www.instagram.com/p/B5VSgkEgQCm/">Home</a></li>
#     <li><a href="https://www.w3schools.com/css/css_navbar.asp">News</a></li>
#     <li><a href="https://www.youtube.com/?gl=IN">Contact</a></li>
#     <li style="float:right"><a class="active" href="#about">About</a></li>
#     </ul> ''')


# # Read by txt file
# def about(request):
#     f = open('1.txt', 'r')
#     file_content = f.read()
#     f.close()
#     return HttpResponse(file_content, content_type="text/plain")


''' read by templating'''

def getData(url):
    r = requests.get(url)
    return r.text

def index(request):

    myHtml = getData("https://www.mohfw.gov.in/")
    worldhtml = getData("https://www.worldometers.info/coronavirus/")

    soup = BeautifulSoup(myHtml,'html.parser')
    wsoup = BeautifulSoup(worldhtml,'html.parser')

    myStr = []
    world = []
    for item in soup.find_all("div",class_="site-stats-count"):
        for strong in item.find_all("strong"):
            myStr.append(strong.get_text())

    for witem in wsoup.find_all("div",class_="maincounter-number"):
        for span in witem.find_all("span"):
            world.append(span.get_text())

    print(myStr)
    print(world)

    params = {"Active":myStr[0] ,"Cured":myStr[1] ,"Death":myStr[2] ,"Migrate":myStr[3],"WActive":world[0] ,"WCured":world[1] ,"WDeath":world[2]}
    

    return render(request,'index.html',params)

def analyze(request):
    # Get the Text
    djtext = request.POST.get('text','default')
    # Check checkbox value
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charactercounter = request.POST.get('charactercounter','off')

    # Check which checkbox is on
    if removepunc == "on":

        panctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in panctuations:
                analyzed += char 

        params = {'purpose':'Removed punctuations','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)


    if uppercase == 'on':

        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

        params = {'purpose':'Change to UpperCase','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)    

    if newlineremove == 'on':

        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char


        params = {'purpose':'New Lines Removed','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)  

    if extraspaceremover == 'on':

        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed += char


        params = {'purpose':'Extra Space Removed','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params) 

    if charactercounter == 'on':

        analyzed = 0
        for index,char in enumerate(djtext):
            print(index)
            analyzed = index+1
            # analyzed = len(djtext)
        params = {'purpose':'Extra Space Removed','analyzed_text':analyzed}
        djtext = analyzed

    return render(request,'analyze.html',params)           

   
def about(request):


    return render(request,'about.html')

# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('name','')
#         email = request.POST.get('email','')
#         desc = request.POST.get('desc','')
#         print('name=',name)
#         print('email=',email)

#         contact = Contact(name=name,email=email,desc=desc)
#         contact.save()
     
#         #send_mail(name,desc,email,['bhoyasnehal08@gmail.com'],fail_silently=False)


#         #thank = True
#         return render(request,'contact.html') 

#     return render(request,'contact.html')       

