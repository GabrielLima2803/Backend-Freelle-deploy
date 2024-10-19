from django.db import models
from datetime import datetime
from uploader.models import Image
from .categoria import Categoria

class Projeto(models.Model):
    class StatusChoices(models.IntegerChoices):
        CLOSE = 1, 'Fechado'
        PROGESS = 2, 'Em andamento'
        FINISH = 3, 'Finalizado'

    titulo = models.CharField(max_length=80)
    descricao = models.TextField()
    image_project = models.ForeignKey(Image, related_name="+", on_delete=models.SET_NULL, null=True, blank=True, default=None)
    status = models.IntegerField(choices=StatusChoices.choices)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prazo_entrega = models.DateField()
    proposta_recebida = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    orcamento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_publicada = models.DateField(default=datetime.now)
    categoria = models.ManyToManyField(Categoria, related_name="projetos")

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return f"Projeto - {self.titulo}"
