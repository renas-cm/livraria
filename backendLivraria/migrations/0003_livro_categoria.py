# Generated by Django 4.2.20 on 2025-03-27 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendLivraria', '0002_alter_categoria_options_alter_editora_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='backendLivraria.categoria'),
            preserve_default=False,
        ),
    ]
