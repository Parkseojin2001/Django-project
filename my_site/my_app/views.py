from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, Http404, HttpResponseRedirect
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

# domain.com/my_app/0 ---> domain.com/my_app/sports

def num_page_view(request, num_page):
    topics_list = list(articles.keys()) # ['sports', 'finance', 'politics']
    topic = topics_list[num_page]
    
    return HttpResponseRedirect(topic)
    
    