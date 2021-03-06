# Generated by Django 2.2.8 on 2019-12-06 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0005_edit_modelweights'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allowedproperty',
            options={'ordering': ['model_id'], 'verbose_name_plural': 'Allowed properties'},
        ),
        migrations.AlterField(
            model_name='project',
            name='modelweights_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend_app.ModelWeights'),
        ),
        migrations.CreateModel(
            name='Inference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_app.Dataset')),
                ('modelweights_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_app.ModelWeights')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='inference_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend_app.Inference'),
        ),
    ]
