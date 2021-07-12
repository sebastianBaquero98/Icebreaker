from django.db import models
from context.models import Context

# Create your models here.
class User(models.Model):
    """ El modelo represtan un usuario del juego
    """
    # Nombre completo del usuario
    nombre = models.TextField(blank=False, null=False)

    # Nickname del usuario (No pueden haber repetidos)
    username = models.TextField(blank=False, null=False, unique=True)

    # Puntaje del usuario
    score = models.IntegerField(default=0)

    # Contexto en el que el usuario uso la frase
    contextF = models.OneToOneField(
        Context, 
        on_delete=models.CASCADE,
        default=None,
    )