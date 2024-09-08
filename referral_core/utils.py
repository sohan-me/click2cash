from django.core.exceptions import ObjectDoesNotExist
from .models import ReferralCode, ReferralRelationship

def create_referral_relationship(referred_user, referral_token):
    try:
        # Fetch the referral code object using the token
        referral_code = ReferralCode.objects.get(token=referral_token)
        referrer = referral_code.user
    except ObjectDoesNotExist:
        # Handle the case where the referral code does not exist
        return

    # Create the first level relationship
    ReferralRelationship.objects.create(
        employer=referrer,
        employee=referred_user,
        refer_token=referral_code,
        level=1
    )

    # Create relationships up to level 5
    current_referrer = referrer
    current_level = 1

    while current_level < 5:
        try:
            next_relationship = ReferralRelationship.objects.get(employee=current_referrer)
            current_level += 1

            ReferralRelationship.objects.create(
                employer=next_relationship.employer,
                employee=referred_user,
                refer_token=referral_code,
                level=current_level
            )

            current_referrer = next_relationship.employer
        except ReferralRelationship.DoesNotExist:
            break
