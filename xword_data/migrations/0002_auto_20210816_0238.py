# Generated by Django 3.0.9 on 2021-08-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xword_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
