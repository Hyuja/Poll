# Generated by Django 4.0.3 on 2022-04-27 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_rename_takeendpic_poll_cases_take_endpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='CandidatePic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='candidate',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
