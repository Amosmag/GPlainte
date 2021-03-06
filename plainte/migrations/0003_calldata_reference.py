# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-02 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plainte', '0002_auto_20180122_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calldata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50, verbose_name='Nom')),
                ('Prenom', models.CharField(max_length=50, verbose_name='Prenom')),
                ('Numero', models.CharField(max_length=30, verbose_name='Numero')),
                ('Nationnalite', models.CharField(max_length=50, null=True, verbose_name='Nationalite')),
                ('Operateur', models.CharField(max_length=50, null=True, verbose_name='Operateur')),
                ('Profession', models.CharField(max_length=50, null=True, verbose_name='Profession')),
                ('Adresse', models.CharField(max_length=100, null=True, verbose_name='Adresse')),
                ('Commune', models.CharField(max_length=50, null=True, verbose_name='Commune')),
                ('Categorie_plainte', models.CharField(max_length=50, null=True, verbose_name='Categorie')),
                ('Mail', models.EmailField(max_length=50, null=True, verbose_name='Email')),
                ('Telephone', models.CharField(max_length=30, verbose_name='Telephone')),
                ('Nature_appel', models.CharField(max_length=30, verbose_name='Nature_appel')),
                ('Objet_appel', models.CharField(max_length=100, null=True, verbose_name='Objet')),
                ('Date_constat', models.DateField(null=True, verbose_name='date du constant')),
                ('Reference_fiche', models.CharField(max_length=100, unique=True, verbose_name='Reference')),
                ('Recuperer', models.BooleanField(default=False, verbose_name='Recuperer')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(max_length=10, verbose_name='numero')),
                ('libelle', models.CharField(max_length=50, verbose_name='libelle')),
            ],
        ),
    ]
