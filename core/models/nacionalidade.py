from django.db import models

class Nacionalidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f"${self.nome} - ${self.sigla}"
    
    class Meta:
        verbose_name = "Nacionalidade"
        verbose_name_plural = "Nacionalidades"