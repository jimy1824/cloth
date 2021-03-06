# Generated by Django 3.2.3 on 2021-05-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0005_rename_name_english_categorycomponents_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdesign',
            name='PantsPocket',
        ),
        migrations.RemoveField(
            model_name='productdesign',
            name='sleeve_pockets',
        ),
        migrations.AddField(
            model_name='productdesign',
            name='bottoms',
            field=models.ManyToManyField(blank=True, to='constructor.Bottom'),
        ),
        migrations.AddField(
            model_name='productdesign',
            name='pants_pocket',
            field=models.ManyToManyField(blank=True, to='constructor.PantsPocket'),
        ),
        migrations.AddField(
            model_name='productdesign',
            name='pockets',
            field=models.ManyToManyField(blank=True, to='constructor.Pocket'),
        ),
        migrations.AddField(
            model_name='productdesign',
            name='sleeve_pocket',
            field=models.ManyToManyField(blank=True, to='constructor.SleevePocket'),
        ),
        migrations.AddField(
            model_name='productdesign',
            name='zip',
            field=models.ManyToManyField(blank=True, to='constructor.Zip'),
        ),
        migrations.AlterField(
            model_name='category',
            name='components',
            field=models.ManyToManyField(blank=True, to='constructor.CategoryComponents'),
        ),
        migrations.AlterField(
            model_name='categorycomponents',
            name='key',
            field=models.CharField(help_text='Component Key', max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='productdesign',
            name='Linings',
            field=models.ManyToManyField(blank=True, to='constructor.Lining'),
        ),
        migrations.AlterField(
            model_name='productdesign',
            name='body',
            field=models.ManyToManyField(blank=True, to='constructor.Body'),
        ),
        migrations.AlterField(
            model_name='productdesign',
            name='collars',
            field=models.ManyToManyField(blank=True, to='constructor.Collar'),
        ),
        migrations.AlterField(
            model_name='productdesign',
            name='cuffs',
            field=models.ManyToManyField(blank=True, to='constructor.Cuff'),
        ),
        migrations.AlterField(
            model_name='productdesign',
            name='hems',
            field=models.ManyToManyField(blank=True, to='constructor.Hem'),
        ),
        migrations.AlterField(
            model_name='productdesign',
            name='hoods',
            field=models.ManyToManyField(blank=True, to='constructor.Hood'),
        ),
        migrations.AlterField(
            model_name='productdesign',
            name='pents',
            field=models.ManyToManyField(blank=True, to='constructor.Pants'),
        ),
        migrations.AlterField(
            model_name='productdesign',
            name='ropes',
            field=models.ManyToManyField(blank=True, to='constructor.Rope'),
        ),
        migrations.AlterField(
            model_name='productdesign',
            name='sleeves',
            field=models.ManyToManyField(blank=True, to='constructor.Sleeve'),
        ),
        migrations.AlterField(
            model_name='productdesign',
            name='straps',
            field=models.ManyToManyField(blank=True, to='constructor.Strap'),
        ),
        migrations.AlterField(
            model_name='productdesign',
            name='straps_buckle',
            field=models.ManyToManyField(blank=True, to='constructor.StrapBuckle'),
        ),
    ]
