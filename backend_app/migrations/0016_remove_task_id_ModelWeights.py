# Generated by Django 3.0.3 on 2020-03-19 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0015_add_outputfile_inference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelweights',
            name='task_id',
        ),
    ]