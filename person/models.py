from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Person(models.Model):
    first_name = models.CharField(_('First Name'), max_length=60)
    surname = models.CharField(_('Surname'), max_length=60)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="User"
    )

    def __str__(self):
        return self.first_name + ' ' + self.surname
