from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    tn=input('Enter Topic name:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is created')

def insert_Webpage(request):
    tn=input('Enter Topic name:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('Enter a name:')
    u=input('Enter URL:')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('Webpage is created')

def insert_AccessRecord(request):
    tn=input('Enter Topic name:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('Enter a name:')
    u=input('Enter URL:')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d=input('Enter date:')
    a=input('Enter author name:')
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    return HttpResponse('AccessRecord is created')

    