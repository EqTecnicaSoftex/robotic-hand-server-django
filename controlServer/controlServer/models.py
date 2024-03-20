from django.db import models


class Medicine(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    horario = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
