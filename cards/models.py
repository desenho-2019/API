from django.db import models




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
    # republic = models.OneToOneField(

    def __str__(self):
        return ' Republic'
