# Generated by Django 3.1.4 on 2020-12-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0084_auto_20201222_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameterset',
            name='heart_activity_inital',
            field=models.DecimalField(decimal_places=5, default=0.6, max_digits=20),
        ),
        migrations.AlterField(
            model_name='parameterset',
            name='immune_activity_inital',
            field=models.DecimalField(decimal_places=5, default=0.6, max_digits=20),
        ),
    ]
