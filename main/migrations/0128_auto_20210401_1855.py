# Generated by Django 3.1.7 on 2021-04-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0127_auto_20210401_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametersetpaylevel',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
