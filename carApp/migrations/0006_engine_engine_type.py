# Generated by Django 5.2.1 on 2025-06-13 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0005_feature_manufacturer_remove_engine_engine_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='engine',
            name='engine_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
