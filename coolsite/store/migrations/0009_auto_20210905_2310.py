# Generated by Django 3.1.5 on 2021-09-05 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0008_auto_20210905_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='photo',
        ),
        migrations.AddField(
            model_name='book',
            name='big_photo',
            field=models.ImageField(blank=True, upload_to='photos/store/', verbose_name='Большое Фото'),
        ),
        migrations.AddField(
            model_name='book',
            name='small_photo',
            field=models.ImageField(blank=True, upload_to='photos/store/', verbose_name='Маленькое Фото'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='photos/store/new/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
