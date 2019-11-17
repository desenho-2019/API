from django.db import models
from cards.models import Card
from person.models import Person

class Vacancy(models.Model):
    pictures = []
    state = models.BooleanField(default=True)
    card = models.ForeignKey(
        Card,
        related_name = 'vacancies',
        on_delete = models.CASCADE,
        verbose_name = 'card',
        blank=True, null=True
    )

    # class Meta:
    #     abstract = True

    def get_price(self):
        if hasattr(self, 'composite'):
            return self.composite.get_price()
        if hasattr(self, 'leaf'):
            return self.leaf.get_price()

    def get_area(self):
        if hasattr(self, 'composite'):
            return self.composite.get_area()
        if hasattr(self, 'leaf'):
            return self.leaf.get_area()

    def updateState(self):
        self.state = not self.state

class Composite(Vacancy):

    # def add(self, vacancy):
    #     self.vacancies.add(vacancy)
    #     self.save()
    #
    # def remove(self, vacancy):
    #     self.vacancies.remove(vacancy)
    #     self.save()
    #     # leaf = self.vacancies_set.filter(pk=vacancy.pk)
    #     # leaf.composite = None
    #     # leaf.save()

    def get_price(self):
        price = 0
        for vacancy in self.vacancies.all():
            price+= vacancy.get_price()
        return price

    def get_area(self):
        area = 0
        for vacancy in self.vacancies.all():
            area+= vacancy.get_area()
        return area

class Leaf(Vacancy):
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
        verbose_name = 'composite',
        blank=True, null=True
    )

    def get_area(self):
        return self.vacancy.get_area()

    def get_price(self):
        return self.vacancy.get_price()
