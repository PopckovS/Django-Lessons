# Generated by Django 3.1.5 on 2021-09-05 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
