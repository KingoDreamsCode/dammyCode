from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PDFFile
from .models import Blog
from django_use_email_as_username.admin import BaseUserAdmin
from .models import User


class PDFFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'year', 'type', 'category', 'id')
    search_fields = ('title', 'department')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'quote')

admin.site.register(User, BaseUserAdmin)
admin.site.register(PDFFile, PDFFileAdmin)
admin.site.register(Blog, BlogAdmin)
