# Generated by Django 4.1.2 on 2023-04-30 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgenceVoyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('lieu', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='public')),
            ],
        ),
        migrations.CreateModel(
            name='LocationVehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('lieu', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='public')),
                ('tarif', models.DecimalField(decimal_places=4, default=0.0, max_digits=8)),
                ('Disponibilite', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='public')),
                ('tarif', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Itineraire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('tarif', models.DecimalField(decimal_places=4, default=0.0, max_digits=8)),
                ('agence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itineraire', to='taxi.agencevoyage')),
            ],
        ),
    ]
