from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):
    gender_option = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))

    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=10)
    gender = models.CharField(choices=gender_option, max_length=12, blank=True)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username
