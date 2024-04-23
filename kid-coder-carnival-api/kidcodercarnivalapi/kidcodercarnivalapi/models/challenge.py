# This class definition is incomplete and lacks attributes and methods.
from django.db import models


class Challenge(models.Model):
    TYPES = (
        ('mcq', 'Multiple Choice Question'),
        ('code', 'Code Challenge'),
    )
    class Meta:
        db_table = 'challenges'

    type = models.CharField(max_length=10, choices=TYPES)
    question = models.TextField()
    options = models.JSONField()
    correct_answer = models.CharField(max_length=100)

    # This class definition is incomplete and lacks attributes and methods.
    # `from django.db import models` is importing the `models` module from the `django.db` package in
    # Python. This module provides classes and functions that allow you to define database models for your
    # Django application.
    def __str__(self):
        return self.question[:50] + '...' if len(self.question) > 50 else self.question
