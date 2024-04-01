from django.shortcuts import render , redirect
from .forms import DoctorForm
from .models import Doctor
from .models import Doctor 
from django.shortcuts import render, get_object_or_404


def create_data(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('readlist')
        
    else:
        form = DoctorForm()
    return render(request, 'create.html', {'form': form})
 

def read_data(request):

    doctor_list = Doctor.objects.all()

    return render(request,'retrieve.html',{'doctor_list': doctor_list})


def update_data(request,pk):

    doctor = Doctor.objects.get(pk=pk)

    if request.method == 'POST' :
        form = DoctorForm(request.POST,instance=doctor)
        if form.is_valid():
         form.save()
        return redirect('readlist')
    else:
        form = DoctorForm(instance=doctor)
    return render(request,'update.html' , {'form':form})



def delete_data(request,pk):

    doctor = Doctor.objects.get(pk=pk)

    if request.method == 'POST' :

        doctor.delete()
        return redirect('readlist')
    
    return render(request,'delete.html' , {'doctor':doctor})


from django.contrib.auth.forms import UserCreationForm

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('createlist')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})




from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login 


def home_page(request):

    return render(request,'home.html') 

def login_page(request):
    
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
          
            user = form.get_user()
            login(request, user)
        
            return redirect('createlist')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='/login/')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }
    return render(request, 'logout.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def aboutUs(request):
    return render(request,'aboutUs.html')

    