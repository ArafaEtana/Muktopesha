# Generated by Django 4.0.4 on 2022-09-21 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0018_productsubmissionmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsubmissionmodel',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', related_query_name='job_product', to='App_main.jobmodel'),
        ),
    ]