from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


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
    imagem = models.URLField(max_length=200, blank=True, null=True)  # Armazena a URL da imagem
    link = models.URLField(max_length=200, blank=True, null=True)  # Pode armazenar outra URL relacionada ao projeto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Projetos"
        ordering = ['-id']