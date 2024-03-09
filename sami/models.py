from django.db import models

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
]

from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title

class Human(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    education = models.CharField(max_length=100, blank=True, null=True)
    workplace = models.CharField(max_length=100, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.name
