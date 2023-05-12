# Generated by Django 4.1.2 on 2023-04-30 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavorisTaxi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('taxi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.taxi')),
            ],
        ),
        migrations.CreateModel(
            name='FavorisLocationVehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('locationVehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.locationvehicule')),
            ],
        ),
        migrations.CreateModel(
            name='FavorisAgenceVoyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenceVoyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.agencevoyage')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentaireTaxi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('taxi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.taxi')),
            ],
        ),
        migrations.CreateModel(
            name='CommentaireLocationVehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('locationVehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.locationvehicule')),
            ],
        ),
        migrations.CreateModel(
            name='CommentaireAgenceVoyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('agenceVoyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.agencevoyage')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]