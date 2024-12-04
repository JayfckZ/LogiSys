from django.contrib import admin
from .models import Pessoa, Cliente, Funcionario

# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "cpf",
        "email",
        "telefone",
        "endereco",
        "telefone",
        "data_registro",
    )
    search_fields = ("nome", "cpf", "email")
    list_filter = ("nome", "data_registro")


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "cpf",
        "telefone",
        "ativo",
        "endereco",
        "telefone",
        "data_admissao",
    )
    search_fields = ("nome", "cpf", "ativo")
    list_filter = ("nome", "ativo", "data_admissao")
