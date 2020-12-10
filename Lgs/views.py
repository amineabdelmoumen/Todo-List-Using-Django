from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def register(request):
    form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+username)
    context={'form':form}        
    return render(request,'singnin.html', context)

def loginPage(request):
    if request.method=="POST":
        request.POST.get('username')
        request.POST.get('password')
        user=authenticate(username=request.POST.get('username'),
           password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')
            return redirect('loginPage')
    return render(request,'login.html')
def homepage(request): 

    return render(request,'home.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')