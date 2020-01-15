from django.db import models

# Create your models here.

class Pessoa(models.Model):
  GENEROS = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('NB', 'Não-binário'),
    ('O', 'Outros'),
  )
  nome = models.CharField(max_length=255, verbose_name='Nome')
  cpf = models.CharField(max_length=255, verbose_name='CPF')
  email = models.EmailField(max_length=255, verbose_name='E-mail')
  telefone = models.CharField(max_length=255, verbose_name='Telefone')
  genero = models.CharField(max_length=255, verbose_name='Gênero', choices=GENEROS  )
  ativo = models.BooleanField(default=True)

  def __str__(self):
    return self.nome

  