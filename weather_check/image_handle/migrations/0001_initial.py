# Generated by Django 4.0 on 2022-05-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200, verbose_name='图片名')),
                ('file_url', models.CharField(max_length=250, verbose_name='图片URL')),
                ('check_result', models.CharField(blank=True, max_length=100, verbose_name='识别结果')),
                ('check_time', models.DateTimeField(auto_now_add=True, verbose_name='检测时间')),
            ],
            options={
                'verbose_name': '图片检测',
                'verbose_name_plural': '图片检测',
                'db_table': 'image_check',
            },
        ),
    ]