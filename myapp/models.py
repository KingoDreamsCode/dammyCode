import datetime
from os import path
from django.db import models
from django.core.validators import FileExtensionValidator
from PyPDF2 import PdfFileReader
from PIL import Image
import os


class PDFFile(models.Model):
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='Projects/')
    cover_image = models.ImageField(upload_to='Covers/') 