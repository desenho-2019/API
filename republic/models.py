from django.db import models

class Republic(models.Model):
    republic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.republic_name
