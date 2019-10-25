# Generated by Django 2.2.6 on 2019-10-24 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('republic', '0001_initial'),
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('location', models.CharField(max_length=200)),
                ('expenses', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RepublicCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('location', models.CharField(max_length=200)),
                ('expenses', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
                ('ownerRepublic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='republiccard', to='republic.Republic', verbose_name='republic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]