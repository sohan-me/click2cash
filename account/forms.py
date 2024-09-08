from django import forms
from .models import Account, KYC
from django.contrib import messages



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password', 'class':"form-control"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':"form-control"}))
    country_code = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'type':'hidden'}))
    referral_code = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Referral Code', 'class':"form-control"}))
    

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'email', 'country_code', 'phone', 'password', 'referral_code']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        referral_code = cleaned_data.get('referral_code')

        if password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match!')

        if not referral_code:
            self.add_error('referral_code', 'Referral code is required.')

        return cleaned_data
	
    def __init__(self, *args, **kwargs):

            super(RegistrationForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['placeholder']='Username'
            self.fields['first_name'].widget.attrs['placeholder']='First Name'
            self.fields['email'].widget.attrs['placeholder']='Your Email'
            self.fields['phone'].widget.attrs['placeholder']='Your Phone Number'
            self.fields['last_name'].widget.attrs['placeholder']='Last Name'

            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'





