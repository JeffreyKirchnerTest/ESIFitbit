# Generated by Django 3.1.7 on 2021-03-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0122_auto_20210318_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session_subject',
            name='contact_email',
            field=models.CharField(default='abc@123.edu', max_length=300, verbose_name='Subject Email'),
        ),
    ]