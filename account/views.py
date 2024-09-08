from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.conf import settings
from django.contrib import messages, auth
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

# Create your views here.
def RegisterView(request):
    
    if request.user.is_authenticated:
        return redirect('home:home')
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            phone_number = form.cleaned_data['phone']
            country_code = form.cleaned_data['country_code']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            referral_code = form.cleaned_data['referral_code']
            
            user = Account.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone=country_code+phone_number,
                password=password, 
                referral_token=referral_code
                )
            user.save()
            
            current_site = get_current_site(request)
            to_mail = email
            mail_subject = 'Please active your account'
            mail_messages = render_to_string('account/account_verification_email.html', {

            'user':user,
            'domain':current_site,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':default_token_generator.make_token(user),

            })
            
            email_send = EmailMessage(mail_subject, mail_messages, settings.EMAIL_HOST_USER, to=[to_mail])
            email_send.fail_silently = False
            email_send.send()
            
            
            messages.success(request, 'Registration successfull')
            return redirect('account:login')
        else:
            print(form.errors.as_data())
    else:
        form = RegistrationForm()
        
    
    return render(request, 'account/register.html', {'form':form})


def ActivateView(request, uid, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('accounts:log_in')

    else:
        messages.error(request, 'Invalid activation link.')
        return redirect('accounts:register')


def LoginView(request):
    
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in.')
        return redirect('home:home')
    
    if request.method == 'POST':		
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user.is_active == False:
            messages.error(request, 'Please active your account first')
            
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home:home')
        
        else:
            messages.error(request, 'Invalid Username or Password.')
            return redirect('account:login')

    return render(request, 'account/login.html')


@login_required(login_url='account:login')
def LogoutView(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'you are logged out.')
        return redirect('home:home')
    else:
        messages.warning(request, 'you are already logged out.')
        return redirect('account:login')
    
def ForgetPasswordView(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        if '@' in identifier:
            try:
                user = Account.objects.get(email=identifier)
            except Account.DoesNotExist:
                user = None
        else:
            try:
                user = Account.objects.get(username=identifier)
            except Account.DoesNotExist:
                user = None
                
        if user is not None:
            current_site = get_current_site(request)
            to_mail = user.email
            mail_subject = 'Reset your password.'
            mail_messages = render_to_string('account/reset_password_email_form.html', {

            'user':user,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':default_token_generator.make_token(user),

            })	

            send_mail = EmailMessage(mail_subject, mail_messages, to=[to_mail])
            send_mail.fail_silently = False
            send_mail.send()
            messages.success(request, 'Password reset email has been send to your email address.')
            return redirect('account:login')     
        
        else:
            messages.error(request, 'No account associated with this email or username.')
            return redirect('account:forget_password')
        
        
    return render(request, 'account/forget_password_form.html')   
        
        
        
def ResetPasswordValidateView(request, uidb64, token):
    
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

    except(ValueError, TypeError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password.')
        return redirect('account:reset_password')

    else:
        messages.error(request, 'This link has been expired!')
        return redirect('account:login')
    
    
def ResetPasswordView(request):
    
    if request.user.is_authenticated:
        return redirect('home:home')
    
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Your password has been updated.')
            return redirect('account:login')
        else:
            messages.error(request, 'Password does not match.')
            return redirect('account:reset_password')
    return render(request, 'account/reset_password.html')