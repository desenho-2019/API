from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils import six, timezone
from users.models import CustomUser
from republic.models import Republic

class Person(models.Model):

    """
    User gender
    """
    MASCULINO = 1
    FEMININO = 2
    GENDER_TITLE= ((MASCULINO,'Masculino'),
                    (FEMININO,'Feminino'),)

    first_name = models.CharField(_('First Name'), max_length=60)
    surname = models.CharField(_('Surname'), max_length=60)
    phone = models.CharField(_('Phonenumber'),max_length=11,blank=True)
    date_of_birth =models.DateField(_('Birth date'),blank=True,default=timezone.now)
    gender = models.IntegerField(_('Gender'),choices=GENDER_TITLE,blank=True,default=1)
    nationality = models.CharField(_('Nacionality'),max_length=30,blank=True,default='Brasil')
    facebook = models.CharField(_('Facebook'),blank=True,max_length=30)
    google = models.CharField(_('Google +'),blank=True,max_length=30)
    photo = models.ImageField(blank=True)

    user = models.OneToOneField(
        CustomUser,
        #related_name = 'email'
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="CostumUser"
    )    



    Republic = models.ForeignKey(
        Republic,
        related_name = 'members',
        on_delete = models.CASCADE,
        verbose_name = "republic",
        blank = True,
        null = True
    )

    def __str__(self):
        return self.first_name + ' ' + self.surname
