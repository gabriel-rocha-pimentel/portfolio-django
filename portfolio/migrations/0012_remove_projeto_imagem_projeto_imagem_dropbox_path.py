# Generated by Django 5.0.6 on 2024-06-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_projeto_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='imagem',
        ),
        migrations.AddField(
            model_name='projeto',
            name='imagem_dropbox_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
