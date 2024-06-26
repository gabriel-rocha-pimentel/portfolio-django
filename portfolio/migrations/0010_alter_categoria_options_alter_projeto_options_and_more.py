# Generated by Django 5.0.6 on 2024-05-31 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_projeto_imagem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['id'], 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='projeto',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Projetos'},
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(default='default.jpg', upload_to='project_images'),
        ),
    ]
