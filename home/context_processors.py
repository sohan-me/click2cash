from .models import CompanyProfile

def company_profile(request):
    try:
        profile = CompanyProfile.objects.first()
    except CompanyProfile.DoesNotExist:
        profile = None
        
    return dict(company_profile=profile)