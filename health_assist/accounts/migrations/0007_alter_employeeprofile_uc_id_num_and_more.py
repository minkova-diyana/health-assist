# Generated by Django 5.1.3 on 2024-11-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_employeeprofile_uc_id_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='uc_id_num',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='hnfusermodel',
            name='uc_id_number',
            field=models.TextField(unique=True),
        ),
    ]
