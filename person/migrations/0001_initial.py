# Generated by Django 2.2.6 on 2019-10-25 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('republic', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('first_name', models.CharField(max_length=60, verbose_name='First Name')),
                ('surname', models.CharField(max_length=60, verbose_name='Surname')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('Republic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='republic.Republic', verbose_name='republic')),
            ],
        ),
    ]
