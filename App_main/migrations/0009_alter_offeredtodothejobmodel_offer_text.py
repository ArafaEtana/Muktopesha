# Generated by Django 4.0.4 on 2022-09-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0008_offeredtodothejobmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeredtodothejobmodel',
            name='offer_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
