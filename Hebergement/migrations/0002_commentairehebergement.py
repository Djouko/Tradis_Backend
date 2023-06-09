# Generated by Django 4.1.2 on 2023-04-30 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Hebergement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentaireHebergement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hebergement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hebergement.hebergement')),
            ],
        ),
    ]
