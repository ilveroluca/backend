# Generated by Django 3.0.3 on 2020-03-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0013_add_is_single_image_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='inference',
            name='logfile',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='modelweights',
            name='logfile',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]
