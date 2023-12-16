from django.shortcuts import render,redirect
from django.http import HttpResponse
from listings.models import Contact
from django.contrib import messages

def index(request):
    if request.method=='POST':
        n = request.POST['fname']
        e = request.POST['email']
        p= request.POST['phone']
        m = request.POST['message']
        c = Contact(name=n, email=e ,phone=p , message=m )
        c.save()
        messages.success(request, message='Thankyou for the Feedback :)')
        return redirect('index')
    else:
        return render(request,'pages/index.html')

def Diseases(request):
    return render(request, 'pages/Diseases.html')

def Fdisease(request):
    return render(request, 'pages/Fdisease.html')

def healthylife(request):
    return render(request, 'pages/healthylife.html')

#def Appoint(request):
    #return render(request, 'pages/Appoint.html')

def Contacts(request):
    return render(request, 'pages/Contacts.html')

def hindiDiseases(request):
    return render(request, 'pages/hindiDiseases.html')

def hindiFdisease(request):
    return render(request, 'pages/hindiFdisease.html')

def hindihealthylife(request):
    return render(request, 'pages/hindihealthylife.html')