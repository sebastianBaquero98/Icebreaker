from django.db import models

# Create your models here.
class Frase(models.Model):
    """ El modelo representa un frase
        Una frase es un pickup line que se pdoría usar para abrir o durante la conversación
    """
    # Es el contenido de la frase
    contenido = models.TextField(blank=False, null=False)

    # Identificador único de la frase
    id = models.AutoField(primary_key=True)
