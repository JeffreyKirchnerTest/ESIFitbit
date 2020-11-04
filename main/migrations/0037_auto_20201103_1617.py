# Generated by Django 3.1.2 on 2020-11-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_session_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameterset',
            name='heart_activity_inital',
            field=models.DecimalField(decimal_places=10, default=0.6, max_digits=20),
        ),
        migrations.AlterField(
            model_name='parameterset',
            name='heart_parameter_1',
            field=models.DecimalField(decimal_places=10, default=0.5, max_digits=20),
        ),
        migrations.AlterField(
            model_name='parameterset',
            name='heart_parameter_3',
            field=models.DecimalField(decimal_places=10, default=6.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='parameterset',
            name='immune_activity_inital',
            field=models.DecimalField(decimal_places=10, default=0.6, max_digits=20),
        ),
        migrations.AlterField(
            model_name='parameterset',
            name='immune_parameter_1',
            field=models.DecimalField(decimal_places=10, default=0.2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='parameterset',
            name='immune_parameter_2',
            field=models.DecimalField(decimal_places=10, default=4.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='parameterset',
            name='immune_parameter_3',
            field=models.DecimalField(decimal_places=10, default=4.0, max_digits=20),
        ),
    ]