# Generated by Django 5.1.2 on 2024-11-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_result_request_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='forts',
            name='fort_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/fort_images/'),
        ),
    ]
