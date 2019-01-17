from django.db import models
#vai importar o abastract base user para uso de usuário customizado.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#aquele que criamos para ser abstrato com tempo
from core.models import IndexedTimeStampedModel
from .manager import UserManager#no caso o ponto é para dizer que é nessa
class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    karma = models.IntegerField(default=0)
    avatar = models.ImageField(blank=True, default='jotaro.jpg')
    is_staff = models.BooleanField(default=False)

    #user, created = Users.objects.get_or_create()
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username