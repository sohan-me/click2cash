from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

# Create your views here.

def HomeView(request):
    plan = Plan.objects.all()
    feature = Feature.objects.all()
    latest_blogs = Blog.objects.order_by('-created_at')[:3]
    testmonial = Testmonial.objects.all()
    context = {
        'plan':plan,
        'feature':feature,
        'latest_blogs':latest_blogs,
        'testmonial':testmonial,
    }
    return render(request, 'home/index.html', context)


def FaqView(request):
    faq = FAQ.objects.all()
    context = {
        'faq':faq
    }
    return render(request, 'home/FAQ.html', context)


def AboutView(request):
    feature = Feature.objects.all()
    testmonial = Testmonial.objects.all()
    context = {
        'feature':feature,
        'testmonial':testmonial,
    }
    return render(request, 'home/about.html', context)


def BlogView(request):
    list_blogs = Blog.objects.all()
    latest_blogs = list_blogs.order_by('-created_at')[:5]
    
    paginator = Paginator(list_blogs, 3)
    page_number = request.GET.get('page')
    
    try:
        blogs = paginator.page(page_number)
    except PageNotAnInteger:
        blogs = paginator.page(1)  
    except EmptyPage:
        blogs= paginator.page(paginator.num_pages)
    
    context = {
        'blogs':blogs,
        'latest_blogs':latest_blogs,
    }
    return render(request, 'home/blog.html', context)

def SearchBlogView(request):
    latest_blogs = Blog.objects.order_by('-created_at')[:3]
    keyword = request.GET.get('search')
    
    if keyword:
        list_results = Blog.objects.filter(title__icontains=keyword) | Blog.objects.filter(description__icontains=keyword)
    elif keyword == '':
        list_results = Blog.objects.all()
    else:
        list_results = Blog.objects.none()
    
        
    paginator = Paginator(list_results, 3)
    page_number = request.GET.get('page')
    
    try:
        blogs = paginator.page(page_number)
    except PageNotAnInteger:
        blogs = paginator.page(1)  
    except EmptyPage:
        blogs= paginator.page(paginator.num_pages)

    
    context = {
        'keyword':keyword,
        'blogs':blogs,
        'latest_blogs':latest_blogs
    }
    
    return render(request, 'home/search_result.html', context)

def ContactView(request):
    return render(request, 'home/contact.html')

def PlanView(request):
    plan = Plan.objects.all()
    context = {
        'plan':plan
    }
    return render(request, 'home/plan.html', context)


def BlogDetailsView(request, blog_id):
    pass