from django.db import models
from performance.models import Performance


# Create your models here.
class Frase(models.Model):
    """ El modelo representa un frase
        Una frase es un pickup line que se pdoría usar para abrir o durante la conversación
    """
    # Es el contenido de la frase
    contenido = models.TextField(blank=False, null=False)

    # Rendimiento de la frase
    rendimiento = models.OneToOneField(
        Performance, 
        on_delete=models.CASCADE,
        default=None,
    )