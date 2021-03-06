# Generated by Django 3.2.3 on 2021-05-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorycomponents',
            name='name',
            field=models.CharField(help_text='Component Name', max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='categorycomponents',
            name='name_english',
            field=models.CharField(help_text='Component Name in English', max_length=250, unique=True),
        ),
    ]
