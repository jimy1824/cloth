# Generated by Django 3.2.3 on 2021-05-26 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0004_auto_20210526_0648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorycomponents',
            old_name='name_english',
            new_name='key',
        ),
    ]