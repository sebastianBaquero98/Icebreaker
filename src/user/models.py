from django.db import models

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

    