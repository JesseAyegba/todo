# Generated by Django 3.0.8 on 2020-08-16 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
