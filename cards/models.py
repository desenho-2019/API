from django.db import models



class Card(models.Model):
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=20)
    price = models.FloatField()
    location = models.CharField(max_length=200)
    items = []
    expenses = models.CharField(max_length=200)
    comodities = []
    contact = models.IntegerField()
    terms = []
    target_gender = []
    status = None

    def __str__(self):
        return self.title
