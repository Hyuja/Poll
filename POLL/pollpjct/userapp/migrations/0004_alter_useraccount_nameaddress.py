# Generated by Django 4.0.3 on 2022-04-17 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_useraccount_nameaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='nameaddress',
            field=models.CharField(blank=True, default='<django.db.models.fields.CharField><django.db.models.fields.CharField>', max_length=120, null=True),
        ),
    ]
