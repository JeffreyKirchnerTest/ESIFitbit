# Generated by Django 3.1.2 on 2020-11-13 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0054_auto_20201112_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='session_subject',
            name='id_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddConstraint(
            model_name='session_subject',
            constraint=models.UniqueConstraint(fields=('id_number', 'session'), name='Session_subject'),
        ),
    ]
