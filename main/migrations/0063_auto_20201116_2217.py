# Generated by Django 3.1.2 on 2020-11-16 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_auto_20201116_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameters',
            name='heartHelpText',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='parameters',
            name='immuneHelpText',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='parameters',
            name='paymentHelpText',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
