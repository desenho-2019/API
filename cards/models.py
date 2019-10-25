from django.db import models
from republic.models import Republic
from person.models import Person



class Card(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    location = models.CharField(max_length=200)
    items = []
    expenses = models.CharField(max_length=200)
    comodities = []
    contact = models.IntegerField()
    terms = []
    target_gender = ''
    status = None
    cardState = None

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class RepublicCard(Card):
    ownerRepublic = models.ForeignKey(
        Republic,
        related_name = 'republiccard',
        on_delete = models.CASCADE,
        verbose_name = 'republic'
    )

    def __str__(self):
        return 'Republic Card' + self.title

class PersonalCard(Card):
    ownerPersonal = models.ForeignKey(
        Person,
        related_name = 'republiccard',
        on_delete = models.CASCADE,
        verbose_name = 'person'
    )

    def _str_(self):
        return 'Personal Card ' + self.title
