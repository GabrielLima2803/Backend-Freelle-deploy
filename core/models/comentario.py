from django.db import models
from datetime import datetime

class Comentario(models.Model):
    class AvaliacaoChoices(models.IntegerChoices):
        POOR = 1, '1 Estrela'
        AVERAGE = 2, '2 Estrelas'
        GOOD = 3, '3 Estrelas'
        EXCELLENT = 4, '4 Estrelas'
        PERFECT = 5, '5 Estrelas'

    created_at = models.DateField(default=datetime.now)
    avaliacao = models.IntegerField(choices=AvaliacaoChoices.choices)
    comentario = models.TextField()

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

    def __str__(self):
        return f"Comentário ${self.id}: Rating - ${self.avaliacao}"
