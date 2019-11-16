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
    owner = None
    owner_type = None
    update_serializer = "CardSerializer"

    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.title

class RepublicCard(Card):
    owner = models.ForeignKey(
        Republic,
        related_name = 'republiccards',
        on_delete = models.CASCADE,
        verbose_name = 'republic'
    )
    owner_type = "Republic"
    update_serializer = "RepublicCardSerializer"

    def __str__(self):
        return 'Republic Card ' + self.title

class PersonalCard(Card):
    owner = models.ForeignKey(
        Person,
        related_name = 'personalcards',
        on_delete = models.CASCADE,
        verbose_name = 'person'
    )
    owner_type = "Person"
    update_serializer = "PersonalCardSerializer"

    def _str_(self):
        return 'Personal Card ' + self.title
