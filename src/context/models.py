from django.db import models
from user.models import MyUser
from frase.models import Frase

# Create your models here.
class Context(models.Model):
    """ Modelo representa la relación muchos a muchos
        entre Frase y usuario y dice el contexto y
        situación en el que se uso la frase.
    """
    # Lista de Aplicaciones
    arrAplicaciones = [('Instagram', (('Story', 'Story'), ('DM', 'DM'))), ('Tinder', 'Tinder'), ('Bumble', 'Bumble'), ('Twitter', 'Twitter'), ('Otro', 'Otro')]

    # Lista de Aplicaciones
    situaciones = [('A', 'Abrir Conversación'), ('S', 'Seguir Conversación')]

    # En que aplicación se envio
    aplicacionUsada = models.CharField(choices=arrAplicaciones, max_length=120, null=True, blank=True)

    # Situación en la que se uso la frase (Para abrir o seguir una conversación)
    situacionUsada = models.CharField(choices=situaciones, max_length=120, null=True, blank=True)

    # Usuario del contexto
    usuario = models.OneToOneField(
        MyUser, 
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    
    # Frase del contexto
    frase = models.OneToOneField(
        Frase, 
        on_delete=models.CASCADE, 
        default=None,
        null=True,
        blank=True,
    )