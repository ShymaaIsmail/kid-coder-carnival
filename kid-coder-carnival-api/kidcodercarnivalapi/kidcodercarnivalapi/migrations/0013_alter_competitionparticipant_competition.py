# Generated by Django 5.0.4 on 2024-04-29 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidcodercarnivalapi', '0012_alter_competition_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitionparticipant',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_participants', to='kidcodercarnivalapi.competition'),
        ),
    ]
