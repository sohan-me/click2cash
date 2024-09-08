from django.contrib import admin
from .models import Plan, Feature, FAQ, CompanyProfile, Blog, Testmonial

# Register your models here.

@admin.register(Plan)
class AdminPlanView(admin.ModelAdmin):
    list_display = ['title', 'price', 'period', 'ad_limit', 'reffer_bonus']
    list_editable = ['reffer_bonus']
    
    
@admin.register(Feature)
class AdminFeatureView(admin.ModelAdmin):
    list_display = ['title', 'description']
    
    
    
@admin.register(FAQ)    
class AdminFAQview(admin.ModelAdmin):
    list_display = ['question']
    
    
@admin.register(CompanyProfile)
class AdminCompanyProfileView(admin.ModelAdmin):
    list_display = ['email', 'phone', 'location']
    

@admin.register(Blog)
class AdminBlogView(admin.ModelAdmin):
    list_display = ['title', 'author', 'tag', 'created_at']
    list_filter = ['author']
    
    
@admin.register(Testmonial)
class AdminTestmonialView(admin.ModelAdmin):
    list_display = ['name', 'designation', 'comment', 'created_at']