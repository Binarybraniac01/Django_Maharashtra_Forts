# Generated by Django 5.1.2 on 2024-10-31 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_latitude_longitude_result_route_user_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forts',
            fields=[
                ('fort_id', models.AutoField(primary_key=True, serialize=False)),
                ('fort_district', models.CharField(max_length=100)),
                ('fort_name', models.CharField(max_length=100)),
                ('fort_latitude', models.FloatField()),
                ('fort_longitude', models.FloatField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Fort_Details',
        ),
    ]
