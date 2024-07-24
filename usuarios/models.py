from django.db import models
import datetime

class User(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=255)

    def get_idade(self):
        dias = datetime.datetime.now() - datetime.datetime(self.data_nascimento.year, self.data_nascimento.month, self.data_nascimento.day)
        return int(dias.days / 365)