from django.shortcuts import render, redirect
from hotel.models import HotelInfo


def home(request):
    data=HotelInfo.objects.all()
    return render(request, 'home.html',{"data":data})