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

    
