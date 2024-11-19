from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, Http404
# Create your views here.

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'    
}

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        return Http404('404 GENERIC ERROR') # 404.html

def add_view(request, num1, num2):
    # domain.com/my_app/num1/num2 --> num1+num2
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))