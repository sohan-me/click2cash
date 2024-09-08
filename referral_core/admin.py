from django.contrib import admin
from .models import ReferralCode, ReferralRelationship

# Register your models here.

@admin.register(ReferralCode)
class AdminReferralCode(admin.ModelAdmin):
    list_display = ['user', 'token']
    
    
@admin.register(ReferralRelationship)
class AdminReferralRelationship(admin.ModelAdmin):
    list_display = ['employer', 'employee', 'refer_token', 'level']
    
