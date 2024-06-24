from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


class Categoria(models.Model):
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Categorias"
        ordering = ['id']


class Projeto(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=800)
    data = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='static/media', default='default.jpg')
    url = models.URLField(max_length=200, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Projetos"
        ordering = ['-id']


@receiver(post_delete, sender=Projeto)
def delete_project_image(sender, instance, **kwargs):
    # Deletar a imagem associada à instância
    if instance.imagem:
        if os.path.isfile(instance.imagem.path):
            os.remove(instance.imagem.path)
