from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Se usa para crear un usuario 
# Se usa para crear un superUsario
class MyUserManager(BaseUserManager):

    def create_user(self, username, password=None):
        
        if not username:
            raise ValueError("Los usuarios tienen que un usuario")
        user = self.model(
            username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




# Create your models here.
class MyUser(AbstractBaseUser):
    """ El modelo represtan un usuario del juego
    """
    # Nombre completo del usuario
    nombre = models.TextField(blank=False, null=False)

    # Nickname del usuario (No pueden haber repetidos)
    username = models.TextField(blank=False, null=False, unique=True)

    # Puntaje del usuario
    score = models.IntegerField(default=0)

    # Es Admin
    is_admin = models.BooleanField(default=False)

    # Esta Activo
    is_active = models.BooleanField(default=True)

    # Es Staff
    is_staff = models.BooleanField(default=False)

    # Es Superuser
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    
    objects = MyUserManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    

    