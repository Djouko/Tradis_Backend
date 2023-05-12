# Generated by Django 4.1.2 on 2023-04-30 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Site touristique',
                'verbose_name_plural': 'Sites touristiques',
            },
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('lieu', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('attachement', models.FileField(null=True, upload_to='public')),
                ('video', models.FileField(null=True, upload_to='videos/')),
                ('latitude', models.FloatField(default=0.0, null=True)),
                ('longitude', models.FloatField(default=0.0, null=True)),
                ('informations', models.TextField(blank=True)),
                ('local_guide_available', models.BooleanField(default=False)),
                ('prix', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updatedAt', models.DateField(auto_now=True)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.categories')),
            ],
        ),
        migrations.CreateModel(
            name='LocalGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_guide', models.CharField(max_length=255, null=True)),
                ('prenom_guide', models.CharField(max_length=255, null=True)),
                ('presentation_guide', models.TextField(blank=True)),
                ('profile_guide', models.FileField(null=True, upload_to='public')),
                ('numero_telephone', models.CharField(max_length=20, null=True)),
                ('disponibilite', models.BooleanField(default=False)),
                ('cni_guide', models.FileField(null=True, upload_to='public')),
                ('available', models.BooleanField(default=False)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local_guides', to='sites.sites')),
            ],
        ),
        migrations.CreateModel(
            name='FavorisSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.sites')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.sites')),
            ],
        ),
    ]
