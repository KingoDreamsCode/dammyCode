# Generated by Django 5.0 on 2024-01-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0007_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdffile',
            name='price',
            field=models.CharField(default='00.0FCFA', max_length=20),
        ),
    ]
