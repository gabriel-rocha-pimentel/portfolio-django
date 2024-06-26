# Generated by Django 2.2.7 on 2024-05-28 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20240522_2101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projeto',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='projeto',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(default='default.jpg', upload_to='img/'),
        ),
    ]
