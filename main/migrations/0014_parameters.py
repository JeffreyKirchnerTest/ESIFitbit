# Generated by Django 3.1.2 on 2020-10-18 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20201018_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactEmail', models.CharField(default='JohnSmith@abc.edu', max_length=1000)),
                ('experimentTimeZone', models.CharField(default='US/Pacific', max_length=1000)),
                ('maxDailyEarnings', models.DecimalField(decimal_places=2, default=600, max_digits=5)),
                ('siteURL', models.CharField(default='https://www.google.com/', max_length=200)),
                ('invitationTextSubject', models.CharField(default='', max_length=1000)),
                ('invitationText', models.CharField(default='', max_length=10000)),
                ('cancelationTextSubject', models.CharField(default='', max_length=1000)),
                ('cancelationText', models.CharField(default='', max_length=10000)),
                ('consentForm', models.CharField(default='', max_length=50000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Parameters',
                'verbose_name_plural': 'Parameters',
            },
        ),
    ]
