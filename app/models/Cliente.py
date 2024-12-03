from django.db import models
from .Pessoa import Pessoa

class Cliente(Pessoa):
    email = models.EmailField(unique=True)
    data_registro = models.DateTimeField(auto_now_add=True)
