# Generated by Django 3.2.9 on 2021-11-08 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Magasin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiel',
            name='personne',
            field=models.ManyToManyField(to='Magasin.Personne'),
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('materiel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Magasin.materiel')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Magasin.personne')),
            ],
        ),
    ]
