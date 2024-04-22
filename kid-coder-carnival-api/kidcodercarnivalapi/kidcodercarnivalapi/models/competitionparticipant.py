# `from django.db import models` is importing the `models` module from the Django web framework. This
# module provides a set of classes and functions that allow you to define the structure of your
# database tables using Python classes. In this code snippet, the `CompetitionParticipant` class is
# inheriting from `models.Model`, which is a base class provided by Django for defining database
# models.
from django.db import models
from .competition import Competition
from .user import CustomUser

# This class represents a competition participant in a Python program.


class CompetitionParticipant(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    submission_date = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
