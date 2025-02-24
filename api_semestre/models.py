from django.db import models

# Create your models here.

class CadastroFilme(models.Model):
    Nome = models.CharField (max_length=20)
    Imagem = models.ImageField()
    NomeAutor = models.CharField(max_length=30)

class CadastroResenha(models.Model):
    Comentário = models.CharField(max_length=3000)

class CadastroPerfil(models.Model):
    Nome = models.CharField (max_length=20)
    Foto = models.ImageField()
    Bio = models.CharField(max_length=50)