from django.db import models

# Create your models here.



class Movie(models.Model):
    # state_choices = (
    #                 ("ACRE","ACRE"),
    #                 ("ALAGOAS","ALAGOAS"),
    #                 ("AMAPÁ","AMAPÁ"),
    #                 ("AMAZONAS","AMAZONAS"),
    #                 ("BAHIA","BAHIA"),
    #                 ("CEARÁ","CEARÁ"),
    #                 ("DISTRITO FEDERAL","DISTRITO FEDERAL"),
    #                 ("ESPÍRITO SANTO","ESPÍRITO SANTO"),
    #                 ("GOIÁS","GOIÁS"),
    #                 ("MARANHÃO","MARANHÃO"),
    #                 ("MATO GROSSO","MATO GROSSO"),
    #                 ("MATO GROSSO DO SUL","MATO GROSSO DO SUL"),
    #                 ("MINAS GERAIS","MINAS GERAIS"),
    #                 ("PARÁ","PARÁ"),
    #                 ("PARAÍBA","PARAÍBA"),
    #                 ("PARANÁ","PARANÁ"),
    #                 ("PERNAMBUCO","PERNAMBUCO"),
    #                 ("PIAUÍ","PIAUÍ"),
    #                 ("RIO DE JANEIRO","RIO DE JANEIRO"),
    #                 ("RIO GRANDE DO NORTE","RIO GRANDE DO NORTE"),
    #                 ("RIO GRANDE DO SUL","RIO GRANDE DO SUL"),
    #                 ("RONDÔNIA","RONDÔNIA"),
    #                 ("RORAIMA","RORAIMA"),
    #                 ("SANTA CATARINA","SANTA CATARINA"),
    #                 ("SÃO PAULO","SÃO PAULO"),
    #                 ("SERGIPE","SERGIPE"),
    #                 ("TOCANTINS","TOCANTINS"),
    #             )
    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    actors = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    uf = models.CharField(max_length=55, null=True, blank=True)
    # sexo = models.CharField(max_length=1, choices=choices_sexo)
    telefone = models.CharField(max_length=20)
    duration = models.IntegerField()
    rate = models.IntegerField()
