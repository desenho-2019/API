from django.db import models
from cards.models import Card
from person.models import Person

class Vacancy(models.Model):
    area = models.FloatField()
    suite = ''
    pictures = []
    forniture = models.CharField(max_length=100)
    price = models.FloatField()
    _state = None

    card = models.ForeignKey(
        Card,
        related_name = 'vacancies',
        on_delete = models.CASCADE,
        verbose_name = 'card'
    )

    tenant = models.ForeignKey(
        Person,
        related_name = 'vacancies',
        on_delete = models.CASCADE,
        verbose_name = 'person'
    )
