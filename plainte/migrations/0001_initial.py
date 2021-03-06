# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canal', models.CharField(max_length=50, verbose_name='canal')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=50, verbose_name='categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Nationalite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationalite', models.CharField(max_length=50, verbose_name='Nationalite')),
            ],
        ),
        migrations.CreateModel(
            name='Operateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operateur', models.CharField(max_length=50, verbose_name='Operateur')),
            ],
        ),
        migrations.CreateModel(
            name='Plaignant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom')),
                ('prenoms', models.CharField(max_length=50, verbose_name='Prenoms')),
                ('contact', models.CharField(max_length=30, verbose_name='Contect')),
                ('adresse', models.CharField(max_length=100, verbose_name='Adresse')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('date_enregistrement', models.DateField(auto_now_add=True, verbose_name='date d"enregistrement')),
                ('nationalite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plainte.Nationalite', verbose_name='Nationalite')),
            ],
        ),
        migrations.CreateModel(
            name='Plainte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100, unique=True, verbose_name='Reference')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom')),
                ('prenoms', models.CharField(max_length=50, verbose_name='Prenoms')),
                ('contact', models.CharField(max_length=30, verbose_name='Contact')),
                ('adresse', models.CharField(max_length=100, null=True, verbose_name='Adresse')),
                ('email', models.EmailField(max_length=50, null=True, verbose_name='Email')),
                ('nationalite', models.CharField(max_length=50, null=True, verbose_name='Nationalite')),
                ('profession', models.CharField(max_length=50, null=True, verbose_name='Profession')),
                ('date_prise_en_compte', models.DateField(null=True, verbose_name='date de prise en compte')),
                ('etat_dossier', models.CharField(max_length=50, null=True, verbose_name='etat du dossier')),
                ('instructeur', models.CharField(max_length=50, verbose_name='instructeur en charge')),
                ('date_entree', models.DateField(verbose_name='date d"entree')),
                ('date_sortie', models.DateField(null=True, verbose_name='date de sortie')),
                ('analyses', models.TextField(null=True, verbose_name='analyses preliminaires')),
                ('recommandations', models.TextField(null=True, verbose_name='recommandations')),
                ('actions_entreprises', models.TextField(null=True, verbose_name='actions entreprises')),
                ('resultats', models.TextField(null=True, verbose_name='resultats')),
                ('decisions', models.CharField(max_length=300, null=True, verbose_name='decisions')),
                ('conclusion', models.TextField(null=True, verbose_name='conclusion')),
                ('autres_commentaires', models.TextField(null=True, verbose_name='autres commentaires')),
                ('archive', models.CharField(max_length=100, null=True, verbose_name='archive')),
                ('date_enregistrement', models.DateField(auto_now_add=True, verbose_name='date d"enregistrement')),
                ('objet', models.TextField(verbose_name='objet de la plainte')),
                ('delai_traitement', models.CharField(max_length=50, null=True, verbose_name='delai de traitement')),
                ('date_constat', models.DateField(null=True, verbose_name='date du constant')),
                ('canal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plainte.Canal', verbose_name='canal')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plainte.Categorie', verbose_name='categorie')),
                ('operateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plainte.Operateur', verbose_name='Operateur')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=50, verbose_name='Profession')),
            ],
        ),
        migrations.AddField(
            model_name='plaignant',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plainte.Profession', verbose_name='Profession'),
        ),
    ]
