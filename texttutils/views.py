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

    soup = BeautifulSoup(myHtml,'html.parser')

    myStr = ""

    for tr in soup.find_all('tbody')[9].find_all('tr'):
            myStr += tr.get_text()

    myStr = myStr[1:]

    itemList = myStr.split("\n\n")

    states = ["Gujarat"]

    for item in itemList[0:]:
        dataList = item.split("\n")
        # print(dataList)
        if dataList[1] in states:
            print("final list",dataList)
            params = {"state" : dataList[1],"Case":dataList[2] }
            return render(request,'index.html',params)
            
            # print(f"State:-{dataList[0]}\nCase:-{dataList[1]}")




    return render(request,'index.html')

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

