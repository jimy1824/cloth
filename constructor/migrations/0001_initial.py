# Generated by Django 3.2.3 on 2021-05-25 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Sleeve Name', max_length=250)),
                ('body_side', models.CharField(choices=[('front', 'Front'), ('back', 'Back')], max_length=24)),
                ('top_view', models.ImageField(upload_to='uploads/body/top')),
                ('middle_view', models.ImageField(upload_to='uploads/body/middle')),
                ('bottom_view', models.ImageField(upload_to='uploads/body/bottom')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
            },
        ),
        migrations.CreateModel(
            name='Bottom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Bottom Name', max_length=250)),
                ('design_image', models.ImageField(upload_to='uploads/Bottom/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Product Category Name', max_length=250, unique=True)),
                ('components', models.CharField(help_text='Product Components', max_length=250, unique=True)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
            },
        ),
        migrations.CreateModel(
            name='CategoryComponents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Component Name', max_length=250)),
                ('name_english', models.CharField(help_text='Component Name in English', max_length=250)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
            },
        ),
        migrations.CreateModel(
            name='Collar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Collar Name', max_length=250)),
                ('design_image', models.ImageField(upload_to='uploads/collar/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Cuff Name', max_length=250)),
                ('design_image', models.ImageField(upload_to='uploads/Cuff/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Hem Name', max_length=250)),
                ('design_image', models.ImageField(upload_to='uploads/Hem/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Hood Name', max_length=250)),
                ('design_image', models.ImageField(upload_to='uploads/Hood/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Lining Name', max_length=250)),
                ('design_image', models.ImageField(upload_to='uploads/Hem/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PantsPocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Sleeve Pocket Name', max_length=250)),
                ('body_side', models.CharField(choices=[('front', 'Front'), ('back', 'Back')], max_length=24)),
                ('design_image', models.ImageField(upload_to='uploads/Pocket/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Pocket Name', max_length=250)),
                ('design_image', models.ImageField(upload_to='uploads/Pocket/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Rope Name', max_length=250)),
                ('design_image', models.ImageField(upload_to='uploads/Rope/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sleeve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Sleeve Name', max_length=250)),
                ('open_view', models.CharField(choices=[('left', 'Right'), ('right', 'Left')], max_length=24)),
                ('top_view', models.ImageField(upload_to='uploads/salves/top')),
                ('right_view', models.ImageField(upload_to='uploads/salves/left')),
                ('left_view', models.ImageField(upload_to='uploads/salves/right')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
            },
        ),
        migrations.CreateModel(
            name='SleevePocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Sleeve Pocket Name', max_length=250)),
                ('design_image', models.ImageField(upload_to='uploads/Pocket/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Strap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Strap Name', max_length=250)),
                ('design_image', models.ImageField(upload_to='uploads/Strap/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StrapBuckle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Strap Buckle Name', max_length=250)),
                ('design_image', models.ImageField(upload_to='uploads/Buckle/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Pocket Name', max_length=250)),
                ('design_image', models.ImageField(upload_to='uploads/Zip/')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Product Category Name', max_length=250, unique=True)),
                ('front_view', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('back_view', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('Linings', models.ManyToManyField(to='constructor.Lining')),
                ('PantsPocket', models.ManyToManyField(to='constructor.PantsPocket')),
                ('body', models.ManyToManyField(to='constructor.Body')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.category')),
                ('collars', models.ManyToManyField(to='constructor.Collar')),
                ('cuffs', models.ManyToManyField(to='constructor.Cuff')),
                ('hems', models.ManyToManyField(to='constructor.Hem')),
                ('hoods', models.ManyToManyField(to='constructor.Hood')),
                ('ropes', models.ManyToManyField(to='constructor.Rope')),
                ('sleeve_pockets', models.ManyToManyField(to='constructor.SleevePocket')),
                ('sleeves', models.ManyToManyField(to='constructor.Sleeve')),
                ('straps', models.ManyToManyField(to='constructor.Strap')),
                ('straps_buckle', models.ManyToManyField(to='constructor.StrapBuckle')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
            },
        ),
    ]
