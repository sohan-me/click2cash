from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from referral_core.models import ReferralCode
from django.utils.crypto import get_random_string
from referral_core.utils import create_referral_relationship 
from home.models import Plan

# Create your models here.
class AccountManager(BaseUserManager):
    
    def create_user(self, username, email, password=None, referral_token=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        if not username:
            raise ValueError('The username field must be set')
       
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        referral_code = ReferralCode.objects.create(
            token=get_random_string(10), 
            user=user
        )
        
        create_referral_relationship(user, referral_token)
        
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superadmin', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(username=username, email=email, password=password, **extra_fields)
        

class Account(AbstractBaseUser):
    
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    is_verified = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']
    
    objects = AccountManager()
    
    def __str__(self):
        return self.username    
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return self.is_admin
    

class KYC(models.Model):
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='kyc')
    dob = models.DateField()
    nationality = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    identity_doc = models.ImageField(upload_to='kyc/')
    icon = models.ImageField(upload_to='profile/')
    address_line= models.CharField(blank=True, max_length=200)
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=30)
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'KYC'

    def __str__(self):
        return self.user
    
class UserPlan(models.Model):
    plan = models.ForeignKey(Plan, related_name='user_plan', on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user