# Generated by Django 5.0 on 2024-01-06 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(default='Write the body here', max_length=1000)),
                ('quote', models.CharField(default='Motivate with a related quote', max_length=100)),
                ('author', models.CharField(max_length=20)),
                ('blog_image', models.ImageField(upload_to='blogImages')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PDFFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cover_page', models.ImageField(upload_to='covers/')),
                ('category', models.CharField(choices=[('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate')], max_length=20)),
                ('department', models.CharField(choices=[('Electrical Department', 'Electrical Department'), ('Computer Department', 'Computer Department')], max_length=30)),
                ('description', models.CharField(max_length=10000)),
                ('year', models.IntegerField()),
                ('type', models.CharField(choices=[('PREMIUM', 'Premium'), ('TEMPLATE', 'Template')], max_length=10)),
                ('pdf_file', models.FileField(upload_to='Projects/')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
    ]
