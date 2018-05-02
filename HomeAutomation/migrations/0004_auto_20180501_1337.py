# Generated by Django 2.0.1 on 2018-05-01 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HomeAutomation', '0003_auto_20180501_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooleanVariable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('value', models.IntegerField()),
                ('on', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RangeVariable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('value', models.IntegerField()),
                ('min', models.IntegerField(default=0)),
                ('max', models.IntegerField(default=1)),
                ('scale', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ValueVariable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('value', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='variable',
            name='state',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='type',
        ),
        migrations.RemoveField(
            model_name='artifact',
            name='state',
        ),
        migrations.DeleteModel(
            name='ModeType',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.DeleteModel(
            name='Variable',
        ),
        migrations.AddField(
            model_name='valuevariable',
            name='artifact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='HomeAutomation.Artifact'),
        ),
        migrations.AddField(
            model_name='rangevariable',
            name='artifact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='HomeAutomation.Artifact'),
        ),
        migrations.AddField(
            model_name='booleanvariable',
            name='artifact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='HomeAutomation.Artifact'),
        ),
    ]