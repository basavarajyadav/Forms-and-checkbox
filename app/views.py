from pydoc_data.topics import topics
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        #print(request.POST)
        TN=request.POST['topic']
        print(TN)
        T=Topic.objects.get_or_create(topic_name=TN)[0]
        T.save()
        return HttpResponse('Topic data is inserted Successfully')
    return render(request,'insert_topic.html')
def insert_webpage(request):
    Topics=Topic.objects.all()
    d={"ts":Topics}
    if request.method=='POST':
        TN=request.POST['topic']
        WN=request.POST['name']
        WU=request.POST['url']
        T=Topic.objects.get_or_create(topic_name=TN)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=WN,url=WU)[0]
        W.save()
        return HttpResponse('Wepage data is inserted Successfully')
    return render(request,'insert_webpage.html',d)
def insert_Access(request):
    Topics=Topic.objects.all()
    d={"ts":Topics}
    if request.method=='POST':
        TN=request.POST['topic']
        WN=request.POST['name']
        WU=request.POST['url']
        DD=request.POST['date']
        T=Topic.objects.get_or_create(topic_name=TN)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=WN,url=WU)[0]
        W.save()
        D=AccessRecords.objects.get_or_create(name=W, date=DD)[0]
        D.save()
        return HttpResponse('Acces data is inserted Successfully')
    return render(request,'insert_Access.html',d)








def topic_dropdown(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    if request.method=='POST':
        TN=request.POST['topic']
        webpages=Webpage.objects.filter(topic_name=TN)
        d1={'ws':webpages}
        return render(request,'display_webpage.html',d1)
    return render(request,'topic_dropdown.html',d)

def select_multiple(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    if request.method=='POST':
        TNS=request.POST.getlist('topic')
        print(TNS)
        webpages=Webpage.objects.none()
        for i in TNS:
            webpages=webpages|Webpage.objects.filter(topic_name=i)
        d1={'ws':webpages}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_multiple.html',d)

def checkbox(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    
    return render(request,'checkbox.html',d)
