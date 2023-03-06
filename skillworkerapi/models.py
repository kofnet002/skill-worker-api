from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.username


class Client(models.Model):
    gender = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    occupation = (
        ("Student", "Student"),
        ("Lecturer", "Lecturer"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=gender, max_length=20, null=True)
    occupation = models.CharField(choices=occupation, max_length=20, null=True)
    phone_number = models.CharField(max_length=12, null=True)
    location = models.CharField(max_length=250, null=True)
    id_number = models.CharField(max_length=250, null=True)
    pic = models.ImageField(null=True, default='net.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # status = models.BooleanField(default=True, null=True)
    # role_id
    # skill_id

class Worker(models.Model):
    gender = (
    ("Male", "Male"),
    ("Female", "Female"),
    )

    skill = (
        ("Plumbing", "Plumbing"),
        ("Carpentry", "Carpentry"),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=gender, max_length=20, null=True)
    skill = models.CharField(choices=skill, max_length=20, null=True)
    phone_number = models.CharField(max_length=12, null=True)
    location = models.CharField(max_length=250, null=True)
    id_number = models.CharField(max_length=250, null=True)
    pic = models.ImageField(null=True, default='net.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # status = models.BooleanField(default=True, null=True)
    # role_id
    # skill_id