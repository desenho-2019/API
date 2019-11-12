from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import six, timezone



class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    
    """
    User gender
    """
    MASCULINO = 1
    FEMININO = 2
    GENDER_TITLE= ((MASCULINO,'Masculino'),
                    (FEMININO,'Feminino'),)

    
    username =None
    name = models.CharField(_('Nome'), max_length=100, blank=True)
    email = models.EmailField(_('Email'),unique=True)
    phone = models.CharField(_('Telefone'),max_length=11)
    date_of_birth =models.DateField(_('Data de Nascimento'))
    gender = models.IntegerField(_('Genero'),choices=GENDER_TITLE)
    nationality = models.CharField(_('Nascionalidade'),max_length=30)
    facebook = models.CharField(_('Facebook'),blank=True,max_length=30)
    google = models.CharField(_('Google +'),blank=True,max_length=30)
    photo = models.ImageField(blank=True)
    is_staff = models.BooleanField(_('staff status'),default=False)
    is_active = models.BooleanField(_('active'),default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    
    def __str__(self):
        return self.get_email_field_name()