from django.contrib import admin
from .models import Account, KYC, UserPlan
# Register your models here.
@admin.register(Account)
class AdminAccount(admin.ModelAdmin):
    list_display = ['username', 'email']
    
@admin.register(KYC)
class AdminKYC(admin.ModelAdmin):
    list_display = ['user', 'dob', 'nationality', 'is_approved']
    list_editable = ['is_approved']
    
    
@admin.register(UserPlan)
class AdminUserPlan(admin.ModelAdmin):
    list_display = ['plan', 'user', 'created_at']