from django.db import models
from django.conf import settings
# Create your models here.

class ReferralCode(models.Model):
    token = models.CharField(unique=True, max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="code_master", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.user}_{self.token}"


class ReferralRelationship(models.Model):
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='inviter', verbose_name="inviter", on_delete=models.CASCADE)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='invited', verbose_name="invited", on_delete=models.CASCADE)
    refer_token = models.ForeignKey(ReferralCode, verbose_name="referral_code", on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.employer.username} -> {self.employee.username} (Level {self.level})"


 