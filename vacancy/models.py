from django.db import models
from cards.models import Card
from person.models import Person


class Vacancy(models.Model):
    pictures = []
    forniture = models.CharField(max_length=100)
    _state = None
    card = models.ForeignKey(
        Card,
        related_name = 'vacancies',
        on_delete = models.CASCADE,
        verbose_name = 'card'
    )

    # class Meta:
    #     abstract = True

    def get_price(self):
        pass

    def get_area(self):
        pass

class Composite(Vacancy):

    def add(self, vacancy):
        self.vacancies_set.add(vacancy)
        self.save()

    def remove(self, vacancy):
        self.vacancies.remove(vacancy)
        self.save()
        # leaf = self.vacancies_set.filter(pk=vacancy.pk)
        # leaf.composite = None
        # leaf.save()

    def get_price(self):
        price = 0
        for vacancy in self.vacancies:
            price+= vacancy.get_price()
        return price

    def get_area(self):
        area = 0
        for vacancy in self.vacancies:
            area+= vacancy.get_area()
        return area

class Leaf(Vacancy):
    tenant = models.ForeignKey(Person, related_name = 'vacancies', on_delete = models.CASCADE, verbose_name = 'person')
    price = models.FloatField()
    area = models.FloatField()

    def get_price(self):
        return self.price

    def get_area(self):
        return self.area

class Middleware(models.Model):
    vacancy = models.OneToOneField(
        Vacancy,
        related_name = 'vacancy',
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="middleware"
    )
    composite = models.ForeignKey(
        Composite,
        related_name = 'vacancies',
        on_delete = models.CASCADE,
        verbose_name = 'composite'
    )

    def get_area(self):
        return vacancy.get_area()

    def get_price(self):
        return vacancy.get_price()
