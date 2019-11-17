from django.contrib import admin
from .models import Composite, Leaf

admin.site.register(Composite)
admin.site.register(Leaf)
