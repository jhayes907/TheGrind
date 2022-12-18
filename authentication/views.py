import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.core.mail import EmailMessage
from validate_email import validate_email
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator

# Create your views here.


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters.'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry that username is taken, please choose another.'}, status=409)

        return JsonResponse({'username_valid': True})


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid.'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry that email is taken, please choose another.'}, status=409)

        return JsonResponse({'email_valid': True})


class RegistrationView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        messages.success(request, 'Success .')
        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():

                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'authentication/register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()

                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain
                link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})

                activate_url = 'https://'+domain+link

                email_subject='Welcome aboard!'
                email_body='Hello '+user.username+' please click the link below to activate your account!\n' +activate_url
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semicolon.com',
                    [email],
                )

                email.send(fail_silently=False)
                messages.success(request, 'Success! Your account was created!')
                return render(request, 'register.html')

        return render(request, 'register.html')



class VerificationView(View):
    def get(self, request, uidb64, token):

        try:
            # tried a force_str over force)_text
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')

            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass
        
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' +user.username+ ' you are now logged in') 
                    return redirect('home')
                messages.error(request, 'Account has not been validated. Please check your email for the activation link.')
                return render(request, 'login.html')

            messages.error(request, 'One of theses fields is not correct.')
            return render(request, 'login.html')

        messages.error(request, 'Please complete both fields to login.')
        return render(request, 'login.html')

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')

        # messages.warning(request, 'Warning yooooooo.')
        # messages.info(request, 'Info yooooooo.')
        # messages.error(request, 'Error yooooooo.')
        # return render(request, 'register.html')
