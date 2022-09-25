# Generated by Django 4.0.4 on 2022-09-21 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_auth', '0011_feeedbackmodel_freelancerprofilemodel_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freelancerprofilemodel',
            name='feedback',
        ),
        migrations.AddField(
            model_name='freelancerprofilemodel',
            name='feedback',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='App_auth.feeedbackmodel'),
        ),
    ]
