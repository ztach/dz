# Generated by Django 4.1.6 on 2023-02-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dzielnia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='komisja',
            name='dzien',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='komisja',
            name='godzina',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='komisja',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]