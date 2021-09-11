from django.shortcuts import render
from App_Login.froms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
# Create your views here.

def sign_up(request):
    form=CreateNewUser()
    registered=False
    if request.method=='POST':
        form= CreateNewUser(dtat=request.POST)
        if form.is_valid():
            user=form.save()
            registered=True
            pass
    return render(request,'App_Login/signup.html', context={'title':'Sign up . TripMate', 'form': form})