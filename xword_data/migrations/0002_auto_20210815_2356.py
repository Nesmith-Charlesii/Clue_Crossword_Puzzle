# Generated by Django 3.0.9 on 2021-08-16 03:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('xword_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='theme',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entry',
            name='entry_text',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]