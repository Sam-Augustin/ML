from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Appoint
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def appoint(request):
    if request.method=='POST':    
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        livestock = request.POST['Livestockowned']
        phone = request.POST['phone']
        address = request.POST['address']
        symptoms = request.POST['DiseaseSymptoms']
        date = request.POST['date']
        time = request.POST['time']
        doctor = request.POST['doctor']
        a = Appoint(fname=fname, lname=lname, livestock=livestock ,phone=phone ,address=address , symptoms=symptoms, date=date , time=time , doctor=doctor )
        a.save()
        messages.success(request, 'Successfully Booked appointment')
        return redirect('index')
        

    else:
        
        return render(request, 'pages/Appoint.html')

@login_required
def adetails(request):
    user=User.objects.get(username=request.user)
    fn=user.first_name
    
    details=Appoint.objects.filter(doctor=fn)
    messages.success(request, 'you are successfully logged in')
    return render(request,'listings/adetails.html',{'details':details,'count':1})
    
