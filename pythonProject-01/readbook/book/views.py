from django.shortcuts import render, get_object_or_404
from .models import Story, Category
from django.core.paginator import Paginator
from django.db.models import Q
import random

def story_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    stories = Story.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        stories = stories.filter(category=category)

    paginator = Paginator(stories, 4)  # 4 stories per page
    page = request.GET.get('page')
    stories = paginator.get_page(page)

    all_story=list(Story.objects.all())
    recent_story=all_story[:3]

    return render(request, 'book/story_list.html', {
        'categories': categories,
        'stories': stories,
        'category': category,
        'page': page,
        'recent_story':recent_story,
    })


def story_detail(request, id):
    story = get_object_or_404(Story, id=id)
    return render(request, 'book/story_detail.html', {'story': story})


def search_story(request):
    query = request.GET.get("search", "")
    results = Story.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)) if query else []

    return render(request, 'book/search.html', {'query': query, 'results': results})

