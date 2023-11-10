# Generated by Django 4.2.5 on 2023-11-09 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metro_wiki', '0028_alter_depot_lines_alter_depot_main_line'),
        ('users', '0003_alter_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='tracked_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='metro_wiki.city', verbose_name='Отслеживаемый метрополитен'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
