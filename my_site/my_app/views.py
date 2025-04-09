from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def simple_view(request):
    return render(request, 'my_app/example.html')  #.html
    
    