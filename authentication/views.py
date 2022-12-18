from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib import messages
# from django.views.decorators.csrf import requires_csrf_token
from validate_email import validate_email

# Create your views here.

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric characters.'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'Sorry that username is taken, please choose another.'}, status=409)


        return JsonResponse({'username_valid': True})


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error':'Email is invalid.'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'Sorry that email is taken, please choose another.'}, status=409)


        return JsonResponse({'email_valid': True})



class RegistrationView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }



        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():

                if len(password)<6:
                    messages.error(request,'Password too short')
                    return render(request, 'authentication/register.html',context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, 'Success! Your account was created!')


        return render(request, 'register.html')


        




        messages.success(request, 'Success youbetcha.')
        messages.warning(request, 'Warning yooooooo.')
        messages.info(request, 'Info yooooooo.')
        messages.error(request, 'Error yooooooo.')
        return render(request, 'register.html')