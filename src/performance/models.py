from django.db import models

# Create your models here.
class Performance(models.Model):
    """ Modelo contiene indicadores para cada frase
    """
    # Representa numero de veces que se uso la frase
    numVecesUsado = models.IntegerField

    # Representa numero de veces que salio la frase en la ruleta
    numVecesSalio = models.IntegerField

    # Representa numero de veces que se uso con éxito
    numVecesExitoso = models.IntegerField

    # Guarda el contexto en el que fue usado la frase [Abrir conversacion o Durante la conversación]
    contextoUsado = models.CharField(max_length=120)

    # Guarda en que aplicación se uso Ejemplos: [Instagram, Facebook, Tinder, Bumble, Twitter]
    aplicacionUsada = models.CharField(max_length=120) 