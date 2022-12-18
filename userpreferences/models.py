from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserPreferences(models.Model):
    user=models.OneToOneField(to=User, on_delete=models.CASCADE)
    language=models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return str(self.user)+'s' + 'preferences'
