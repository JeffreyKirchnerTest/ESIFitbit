# Generated by Django 3.1.4 on 2021-03-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0097_auto_20210301_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='session_subject_questionnaire2',
            name='gender_identity',
            field=models.CharField(choices=[('', ''), ('Man', 'Man'), ('Woman', 'Woman'), ('FillIn', 'Specify Below')], default='Man', max_length=100, verbose_name='To which gender identity do you most identify?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session_subject_questionnaire2',
            name='gender_identity_fillin',
            field=models.CharField(default='', max_length=1000, verbose_name='To which gender identity do you most identify (Fill in)?'),
        ),
        migrations.AddField(
            model_name='session_subject_questionnaire2',
            name='sex_at_birth',
            field=models.CharField(choices=[('', ''), ('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=100, verbose_name='What was your sex at birth?'),
            preserve_default=False,
        ),
    ]