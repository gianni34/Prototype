# Generated by Django 2.0.1 on 2018-05-21 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('HomeAutomation', '0004_auto_20180501_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='booleanvariable',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_homeautomation.booleanvariable_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='rangevariable',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_homeautomation.rangevariable_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='valuevariable',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_homeautomation.valuevariable_set+', to='contenttypes.ContentType'),
        ),
    ]