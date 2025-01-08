# Generated by Django 5.1.3 on 2025-01-08 08:12

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_alter_reimbursementclaims_document_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='type_document',
        ),
        migrations.RemoveField(
            model_name='packages',
            name='name',
        ),
        migrations.RemoveField(
            model_name='underpackages',
            name='coverage',
        ),
        migrations.RemoveField(
            model_name='underpackages',
            name='limit',
        ),
        migrations.RemoveField(
            model_name='underpackages',
            name='name',
        ),
        migrations.CreateModel(
            name='DocumentsTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('type_document', models.CharField(max_length=100)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='packages.documents')),
            ],
            options={
                'verbose_name': 'documents Translation',
                'db_table': 'packages_documents_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='PackagesTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='packages.packages')),
            ],
            options={
                'verbose_name': 'packages Translation',
                'db_table': 'packages_packages_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='UnderPackagesTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100)),
                ('limit', models.CharField(max_length=255)),
                ('coverage', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='packages.underpackages')),
            ],
            options={
                'verbose_name': 'under packages Translation',
                'db_table': 'packages_underpackages_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
