# Generated by Django 2.2.7 on 2019-12-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0004_big_refactor'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelweights',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]