# Generated by Django 3.1.7 on 2022-01-29 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220129_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='video',
            field=models.FileField(blank=True, default='default_files/default.mp4', upload_to='Lapp_files/videos/Wapp_files/videos/Tapp_files/videos/Rapp_files/videos/Eapp_files/videos/Kapp_files/videos/Uapp_files/videos/Papp_files/videos/Zapp_files/videos/7'),
        ),
    ]
