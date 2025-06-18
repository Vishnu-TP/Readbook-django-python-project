from django.urls import path
from . import views

app_name = 'book'  # Namespace for URL mapping

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('category/<slug:category_slug>/', views.story_list, name='story_category'),
    path('story/<int:id>/', views.story_detail, name='story_detail'),
    path('search/', views.search_story, name='search_story'),  # Corrected search URL
]
