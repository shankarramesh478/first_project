from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def jampandu(request):
    return HttpResponse('<h1><marquee scrollamount="30px">hi jampandu </h1></marquee>')


def darling(request):
    return HttpResponse('<h1><marquee scrollamount="50px" behavior="alternate" loop="5" >HII DARLING you so cute yaar</h1></marquee>')