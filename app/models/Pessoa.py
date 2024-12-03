from django.db import models
from django.core.validators import RegexValidator


class Pessoa:
    id = models.AutoField(unique=True, primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(
        max_length=14,
        unique=True,
        validators=[
            RegexValidator(
                regex="^\d{3}\.\d{3}\.\d{3}-\d{2}\$",
                message="O CPF deve estar no formato XXX.XXX.XXX-XX.",
            )
        ],
    )
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex="^\d{2}\ \d{5}\-\d{4}\$",
                message="O telefone deve estar no formato XX XXXXX-XXXX",
            )
        ],
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

    def formataCpf(self):  # Formata o CPF caso não esteja no padrão com pontuação.
        cpf = self.cpf
        if len(cpf) == 11:
            cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

        return cpf

    def formataTel(self):  # Formata o telefone caso não esteja no padrão com pontuação.
        tel = self.telefone
        if len(tel) == 11:
            tel = f"{tel[:2]} {tel[2:7]}-{tel[7:]}"

        elif len(tel) == 12:
            tel = f"{tel[:2]} {tel[3:8]}-{tel[8:]}"

        return tel
