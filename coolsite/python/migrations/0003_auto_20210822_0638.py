# Generated by Django 3.2.6 on 2021-08-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python', '0002_alter_python_section_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='python_lesson',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='python_section',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
