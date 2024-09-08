from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Plan(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField()
    period = models.PositiveIntegerField()
    ad_limit = models.PositiveIntegerField()
    reffer_bonus = models.CharField(default='N/A', max_length=100)
    tag= models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    def get_price(self):
        return int(self.price)
    
    
class Feature(models.Model):
    icon = models.ImageField(upload_to='uploads/features/', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
    
class CompanyProfile(models.Model):
    
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)    
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Company Profile Info'
    
    def __str__(self):
        return f'{self.email} - {self.phone}'
    


    
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='blogs/', null=True, blank=True)
    author = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

    
    
class Testmonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='testmonial/', null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name