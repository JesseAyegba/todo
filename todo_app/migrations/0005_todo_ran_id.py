# Generated by Django 3.0.8 on 2020-08-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_auto_20200728_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='ran_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]