# Generated by Django 5.1.3 on 2024-11-25 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_employeeprofile_uc_id_number_hashed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeprofile',
            old_name='uc_id_number_hashed',
            new_name='uc_id_num',
        ),
    ]
