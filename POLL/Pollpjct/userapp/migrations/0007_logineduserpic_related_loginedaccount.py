# Generated by Django 4.0.3 on 2022-04-26 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_logineduserpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='logineduserpic',
            name='related_loginedaccount',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.logineduseraccount'),
        ),
    ]
