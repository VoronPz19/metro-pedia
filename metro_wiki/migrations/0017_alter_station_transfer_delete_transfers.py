# Generated by Django 4.2.5 on 2023-10-24 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro_wiki', '0016_transfers_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='transfer',
            field=models.ManyToManyField(blank=True, related_name='+', to='metro_wiki.station', verbose_name='Пересадки'),
        ),
        migrations.DeleteModel(
            name='Transfers',
        ),
    ]
