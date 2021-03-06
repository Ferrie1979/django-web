# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('nom_empresa', models.CharField(max_length=40)),
                ('mail_empresa', models.EmailField(max_length=80)),
                ('tlf_empresa', models.CharField(max_length=9)),
                ('adr_empresa', models.CharField(max_length=80)),
                ('cp_empresa', models.CharField(max_length=5)),
                ('logo_empresa', models.ImageField(upload_to='uploads', verbose_name='Empresa_Imatge')),
            ],
        ),
    ]
