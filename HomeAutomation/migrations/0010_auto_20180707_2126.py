# Generated by Django 2.0.1 on 2018-07-08 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeAutomation', '0009_auto_20180707_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='answer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='question',
            field=models.CharField(max_length=100, null=True),
        ),
    ]