from django.db import models

class Colaborador(models.Model):
    nome=models.CharField(max_length=30)
    nascimento=models.DateField()
    rg=models.CharField(max_length=10)
    cpf=models.CharField(max_length=14)
    sexo_choices=(
        ('M', 'M'),
        ('F', 'F'),
    )
    sexo_choices=models.CharField(max_length=2, choices=sexo_choices)

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    colaborador=models.ForeignKey(Colaborador,on_delete=models.CASCADE)
    tipo_choices=(
        ('Graduação','Graduação'),
        ('Pós-Graduação','Pós-Graduação'),
        ('Mestrado','Mestrado'),
        ('Doutorado','Doutorado'),
        ('Extensão','Extensão'),
        ('Certificação','Certificação')
    )
    tipo=models.CharField(max_length=15,choices=tipo_choices)
    nome_curso=models.CharField(max_length=50)
    instituicao=models.CharField(max_length=50)
    dt_inicio=models.DateField()
    dt_termino=models.DateField()

    def __str__(self):
        return self.nome_curso