# Generated by Django 5.1.3 on 2024-11-27 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0009_alter_employeeprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_document', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReimbursementClaims',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UnderPackages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('limit', models.CharField(max_length=255)),
                ('coverage', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='under_packages', to='accounts.insuredcompanies')),
                ('documents_needed', models.ManyToManyField(blank=True, null=True, to='packages.documents')),
                ('packages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packages', to='packages.packages')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPackages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_packages', to='accounts.insuredcompanies')),
                ('packages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_under_packages', to='packages.underpackages')),
            ],
        ),
    ]