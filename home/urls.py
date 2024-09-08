from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('faq/', views.FaqView, name='faq'),
    path('about/', views.AboutView, name='about'),
    path('plans/', views.PlanView, name='plan'),
    path('contact/', views.ContactView, name='contact'),
    path('blog/', views.BlogView, name='blog'),
    path('blog/read/<int:id>/', views.BlogDetailsView, name='blog_details'),
    path('blog/search-result/', views.SearchBlogView, name='search_blog'),
    
]