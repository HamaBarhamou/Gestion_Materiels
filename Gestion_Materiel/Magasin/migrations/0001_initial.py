# Generated by Django 3.2.9 on 2021-11-06 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gerant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Magasin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('gerant', models.ManyToManyField(to='Magasin.Gerant')),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('fonction', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TypeMateriel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Materiel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('caracteristique', models.CharField(max_length=50)),
                ('magasin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Magasin.magasin')),
                ('typemateriel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Magasin.typemateriel')),
            ],
        ),
    ]
