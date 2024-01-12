from django.contrib import admin
from django_use_email_as_username.admin import BaseUserAdmin

from .models import User
from django.contrib.auth.admin import UserAdmin
from .models import PDFFile
from .models import Blog
from .models import Room, Message, ContactForm


class PDFFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'year', 'type', 'category', 'id', 'price')
    search_fields = ('title', 'department')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'quote')

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(PDFFile, PDFFileAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Room)
admin.site.register(Message)

admin.site.register(User, BaseUserAdmin)


admin.site.register(ContactForm, ContactFormAdmin)

