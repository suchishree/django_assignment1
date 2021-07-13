from django.db import models

class RegistrationModel(models.Model):
    Name = models.CharField(max_length=30, null=False)
    contact = models.IntegerField(unique=True, null=False)
    email = models.EmailField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=30, null=False)
    otp = models.IntegerField(null=False, default=0000)
    status = models.CharField(max_length=30, null=False, default="pending")
    datetime = models.DateTimeField(auto_now_add=True)