
from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.

def register(request):
    EUFO = UserForm()
    EPFO = ProfileForm()
    d = {'EUFO':EUFO,'EPFO':EPFO}
    if request.method == 'POST' and request.FILES:
        UFDO = UserForm(request.POST)
        PFDO = ProfileForm(request.POST, request.FILES)
        if UFDO.is_valid():
            MUFDO = UFDO.save(commit=False)
            pw = UFDO.cleaned_data.get('password')
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = PFDO.save(commit=False)
            MPFDO.username = MUFDO
            MPFDO.save()
            return HttpResponse('User registration is Done')
        return HttpResponse('invalid Data')
    return render(request, 'registration.html', d)
