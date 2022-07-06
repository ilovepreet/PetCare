from multiprocessing import context
from django.shortcuts import render
from home . models import Contact , Suggest
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def suggest(request):
    if request.method=="POST":
        sname = request.POST.get('sname')
        smessage = request.POST.get('smessage')
        suggest = Suggest(sname=sname,smessage=smessage)
        suggest.save()
        messages.success(request,"Submit Successfully!")
    return render(request,'suggest.html')

def sugg(request):
    suggestions = Suggest.objects.all()
    print(suggestions)
    context = {'sugg': suggestions}
    return render(request,'sugg.html', context)

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        textarea = request.POST.get('textarea')
        contact = Contact(name=name, phone=phone, textarea=textarea)
        contact.save()
        messages.success(request,"Submit Successfully! ")
    return render(request,'contact.html')
