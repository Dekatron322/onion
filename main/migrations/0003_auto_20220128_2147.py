# Generated by Django 3.1.7 on 2022-01-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220128_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='video',
            field=models.FileField(blank=True, default='default_files/default.mp4', upload_to='Lapp_files/videos/Napp_files/videos/6app_files/videos/Napp_files/videos/Lapp_files/videos/Napp_files/videos/Aapp_files/videos/Sapp_files/videos/4app_files/videos/W'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='video',
            field=models.FileField(blank=True, default='default_files/default.mp4', upload_to='Capp_files/videos/Capp_files/videos/4app_files/videos/8app_files/videos/Oapp_files/videos/9app_files/videos/Kapp_files/videos/Zapp_files/videos/Lapp_files/videos/Q'),
        ),
    ]
