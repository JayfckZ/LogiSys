from django.db import models
from .Pessoa import Pessoa

class Funcionario(Pessoa):
    data_admissao = models.DateField()
    ativo = models.BooleanField(default=True)
