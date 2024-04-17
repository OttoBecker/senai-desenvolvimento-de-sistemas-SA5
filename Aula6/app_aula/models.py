from django.db import models

# Create your models here.
class Pessoas(models.Model):
    """
    -
    Fields:
    - `nome` = String
    - `email` = String
    - `nascimento` = Date
    """
    #ID é gerado automaticamente
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nascimento = models.DateField()
    pais = models.CharField(max_length=50)

    # data_criacao = models.DateField()