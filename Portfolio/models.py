from django.db import models

# Create your models here.
class About(models.Model):
    about_text = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=50)

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=30)

class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    description = models.TextField()

class ContactForm(models.Model):
    name = models.TextField()
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField