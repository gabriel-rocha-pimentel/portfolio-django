# Generated by Django 5.0.6 on 2024-06-24 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_remove_projeto_imagem_dropbox_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='imagem',
            field=models.URLField(blank=True, null=True),
        ),
    ]