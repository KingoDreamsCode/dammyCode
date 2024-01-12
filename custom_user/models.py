from django_use_email_as_username.models import BaseUser, BaseUserManager
from django.db import models
import datetime
from os import path
from django.core.validators import FileExtensionValidator
from PyPDF2 import PdfFileReader
from PIL import Image
import os
from datetime import datetime


class PDFFile(models.Model):
    CATEGORY_CHOICES = [
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
    ]

    DEPARTMENT_CHOICES = [
        ('Electrical Department', 'Electrical Department'),
        ('Computer Department', 'Computer Department'),
    ]

    TYPE_CHOICES = [
        ('PREMIUM', 'Premium'),
        ('TEMPLATE', 'Template'),
    ]

    title = models.CharField(max_length=200)
    cover_page = models.ImageField(upload_to='covers/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
    description = models.CharField(max_length=10000)
    year = models.IntegerField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    pdf_file = models.FileField(upload_to='Projects/')
    price = models.CharField(max_length = 20, default = "00.0FCFA")

    def __str__(self):
        return self.title

class Blog(models.Model):
    body = models.CharField(max_length=1000, default =  "Write the body here")
    quote = models.CharField(max_length = 100, default = "Motivate with a related quote")
    author =models.CharField(max_length = 20)
    blog_image = models.ImageField(upload_to= 'blogImages')

class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default = datetime.now, blank = True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=1000)


class User(BaseUser):
    objects = BaseUserManager()
    username = models.CharField(max_length=150)

    def __str__(self):
        return self.username


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
