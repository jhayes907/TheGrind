from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import UserPreferences
from django.contrib import messages
# Create your views here.


def general(request):
    language_data = []
    file_path = os.path.join(settings.BASE_DIR, 'languages.json')

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for k, v in data.items():
            language_data.append({'name': k, 'value': v})
   
    exists = UserPreferences.objects.filter(user=request.user).exists()
    user_preferences = None

    if exists:
        user_preferences = UserPreferences.objects.get(user=request.user)
    
    if request.method == 'GET':

    # This is for changing a json file to display as list in dropdown selectors
        return render(request, 'general.html', {'languages': language_data, 'user_preferences': user_preferences})
    else:
        language = request.POST['language']

        if exists:
            user_preferences.language = language
            user_preferences.save()
        else:
            UserPreferences.objects.create(user=request.user, language=language)
        messages.success(request, 'Changes saved successfully')

        return render(request, 'generaL.html', {'languages': language_data, 'user_preferences': user_preferences})


def account(request):
    return render(request, 'account.html')
