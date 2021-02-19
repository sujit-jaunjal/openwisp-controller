# Generated by Django 3.1.6 on 2021-02-11 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openwisp_users', '0011_user_first_name_150_max_length'),
        ('connection', '0005_device_connection_failure_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='name',
            field=models.CharField(db_index=True, max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='credentials', unique_together={('name', 'organization')}
        ),
    ]
