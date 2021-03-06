# Generated by Django 3.2.3 on 2021-05-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0003_auto_20210526_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='key',
            field=models.CharField(default=1, help_text='Product Category Key', max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='category',
            name='components',
        ),
        migrations.AddField(
            model_name='category',
            name='components',
            field=models.ManyToManyField(to='constructor.CategoryComponents'),
        ),
    ]
