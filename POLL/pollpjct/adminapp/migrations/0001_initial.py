# Generated by Django 4.0.3 on 2022-04-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CandidateName', models.CharField(max_length=20)),
                ('side', models.CharField(max_length=50)),
                ('CandidateNum', models.CharField(max_length=3)),
                ('votes', models.IntegerField()),
            ],
        ),
    ]