from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse


def registration(request):
    RFEO=RegistrationFrom()
    d={'RFEO':RFEO}
    if request.method=='POST':
        RFDO=RegistrationFrom(request.POST)
        if RFDO.is_valid():
            return HttpResponse(str(RFDO.cleaned_data))
        # else:
        #     return HttpResponse('Invalid data')
        
    return render(request,'registration.html',d)
# Create your views here.
