# `from django.db import models` is importing the `models` module from the Django web framework. This
# module provides a set of classes and functions that allow you to define the structure of your
# database tables using Python classes. In this code snippet, the `models.Model` class is being used
# to define the `CompetitionChallenge` model as a Django model, which will be translated into a
# database table by Django's ORM (Object-Relational Mapping) system.
from django.db import models
from .competition import Competition
from .challenge import Challenge


# This class likely represents a model for competition challenges in a Python application.
class CompetitionChallenge(models.Model):
    class Meta:
        db_table = 'competition_challenge'

    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
