# Generated by Django 4.1.4 on 2022-12-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_movie_telefone"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="uf",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ACRE", "ACRE"),
                    ("ALAGOAS", "ALAGOAS"),
                    ("AMAPÁ", "AMAPÁ"),
                    ("AMAZONAS", "AMAZONAS"),
                    ("BAHIA", "BAHIA"),
                    ("CEARÁ", "CEARÁ"),
                    ("DISTRITO FEDERAL", "DISTRITO FEDERAL"),
                    ("ESPÍRITO SANTO", "ESPÍRITO SANTO"),
                    ("GOIÁS", "GOIÁS"),
                    ("MARANHÃO", "MARANHÃO"),
                    ("MATO GROSSO", "MATO GROSSO"),
                    ("MATO GROSSO DO SUL", "MATO GROSSO DO SUL"),
                    ("MINAS GERAIS", "MINAS GERAIS"),
                    ("PARÁ", "PARÁ"),
                    ("PARAÍBA", "PARAÍBA"),
                    ("PARANÁ", "PARANÁ"),
                    ("PERNAMBUCO", "PERNAMBUCO"),
                    ("PIAUÍ", "PIAUÍ"),
                    ("RIO DE JANEIRO", "RIO DE JANEIRO"),
                    ("RIO GRANDE DO NORTE", "RIO GRANDE DO NORTE"),
                    ("RIO GRANDE DO SUL", "RIO GRANDE DO SUL"),
                    ("RONDÔNIA", "RONDÔNIA"),
                    ("RORAIMA", "RORAIMA"),
                    ("SANTA CATARINA", "SANTA CATARINA"),
                    ("SÃO PAULO", "SÃO PAULO"),
                    ("SERGIPE", "SERGIPE"),
                    ("TOCANTINS", "TOCANTINS"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]