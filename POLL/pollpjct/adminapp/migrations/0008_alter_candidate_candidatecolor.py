# Generated by Django 4.0.3 on 2022-04-27 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_candidate_candidatecolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='CandidateColor',
            field=models.CharField(default='rgba(, , , )', max_length=25),
        ),
    ]