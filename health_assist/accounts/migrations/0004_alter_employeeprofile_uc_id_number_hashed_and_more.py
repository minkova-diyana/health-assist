# Generated by Django 5.1.3 on 2024-11-21 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_employeeprofile_uc_id_number_hashed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='uc_id_number_hashed',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='hnfusermodel',
            name='uc_id_number',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]