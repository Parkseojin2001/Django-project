from django.urls import path
from . import views

# domaion.com/my_app/simple_view
urlpatterns = [
    path('<int:num_page>', views.num_page_view),
    path('<str:topic>/', views.news_view, name='topic-page'),
  
]
