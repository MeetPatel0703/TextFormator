#I HAVE CREATED THIS FILE - MEET

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def removepunc(request):
    djtext=request.POST.get('text','default')
    rp=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    countchar=request.POST.get('countchar','off')
    nlr=request.POST.get('newlineremover','off')
    if rp=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        djtext=analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if countchar == "on":
        count=0
        for char in djtext:
            count+=1
        params = {'purpose': 'Count the number of character', 'analyzed_text': count}

    if (nlr == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(rp!="on" and fullcaps!="on" and countchar != "on" and nlr != "on"):
        return HttpResponse("Error")

    return render(request,'removepunc.html',params)
