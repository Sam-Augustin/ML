
from django.shortcuts import render,redirect

from django.contrib import messages,auth
from django.contrib.auth.models import User
import pickle

file = open("rf_tuned.pkl",'rb')
object_file = pickle.load(file)
disease={
    0:"Anaplasmosis : पुनर्जनन",
    1:"Ascarids : एस्केरिड्स",
    2:"Avian Influenza : पक्षियों से लगने वाला भारी नज़ला या जुखाम",
    3:"Avian Pox : पक्षियों से लगने वाला चेचक",
    4:"Bloat : फूलना",
    5:"Bluetongue : नीली जीभ",
    6:"Bovine tuberculosis : गोजातीय तपेदिक",
    7:"Bovine viral diarrhea : गोजातीय वायरल डायरिया",
    8:"Brucellosis : ब्रूसिलोसिस",
    9:"Equine encephalomyelitis : इक्वाइन एन्सेफेलोमाइलाइटिस",
    10:"Foot and mouth disease (FMD) : पैर और मुंह की बीमारी (एफएमडी)",
    11:"Hemorrhagic septicemia : रक्तस्रावी सेप्टीसीमिया",
    12:"Infectious Coryza : संक्रामक सर्दी-जुकाम",
    13:"Lumpy skin : ढेलेदार त्वचा",
    14:"Mastitis (bacterial infection) : मास्टिटिस (जीवाणु संक्रमण)",
    15:"Necrotic enteritis : परिगलित आंत्रशोथ",
    16:"Newcastle : न्यूकासल",
    17:"Peste des Petits Ruminants : पेस्ट डेस पेटिट्स जुगाली करने वाले",
    18:"Pneumonia : फेफड़ों की सूजन",
    19:"Rabies : जलांतक",
    20:"Rift Valley fever : दरार घाटी बुखार",
    21:"Sheep Pox : भेड़ चेचक",
    22:"Thrush : थ्रश ",
    23:"Tuberculosis : यक्ष्मा ",

}

def index(request):
    return render(request, 'listings/listings.html')

def listing(request):
 if request.method =='POST':
    username = request.POST['username']
    password = request.POST['password']

    User = auth.authenticate(username = username, password = password)
   
    if User is not None:
        auth.login(request, User)
        
        return redirect('adetials')
    else:
        messages.error(request,'invalid credentials')
        return redirect('listing')
 else:
        return render(request, 'listings/listing.html')
   
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        
       
        password = request.POST['password']
        password2 = request.POST['password2']
        
          
    #check pssd
        if password == password2:
           user = User.objects.create_user(username=username, password=password2, email=email, first_name=first_name, last_name=last_name)
           user.save()
           messages.success(request, 'Successfully registered')
           return redirect('listing')

        else:
            messages.error(request, 'Passwords do not match')
           
            return redirect('register')
        
    else:
        return render(request, 'listings/register.html')

    

def logout(request):
    return redirect(request, 'index')
    
def search(request):
    return render(request, 'listings/search.html')

def prediction(request):
    t=[]
    v=""
    if request.method =='POST':
        var1 = request.POST['DiseaseSymptom1']
        var2 = request.POST['DiseaseSymptom2']
        var3 = request.POST['DiseaseSymptom3']
        var1 = int(var1)
        var2 = int(var2)
        var3 = int(var3)
        
        for i in range(56):
            t.append(0)
        t[var1]=1
        t[var2]=1
        t[var3]=1
        new_var = [t]
        predict =object_file.predict(new_var)
        v=disease[predict[0]]
    return render(request, 'listings/prediction.html',{'v':v})





