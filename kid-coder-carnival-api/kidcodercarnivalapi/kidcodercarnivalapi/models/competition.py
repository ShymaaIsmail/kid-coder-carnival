# `from django.db import models` is importing the `models` module from the `django.db` package in
# Python. This module provides classes and functions that allow you to define database models for your
# Django application. In the provided code snippet, the `Competition` class is inheriting from
# `models.Model`, which allows it to define fields like `title`, `description`, `start_date`, and
# `end_date` as database fields.
from django.db import models
from .challenge import Challenge
from .user import User
# `from django.db import models` is importing the `models` module from the `django.db` package in
# Python. This module provides classes and functions that allow you to define database models for your
# Django application. In the provided code snippet, the `Competition` class is inheriting from
# `models.Model`, which allows it to define fields like `title`, `description`, `start_date`, and
# `end_date` as database fields.


class Competition(models.Model):
    class Meta:
        db_table = 'competitions'

    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    # Define ManyToManyField for challenges and participants
    challenges = models.ManyToManyField(Challenge, related_name='challenges')
    participants = models.ManyToManyField(User, related_name='participants')

    def __str__(self):
        return self.title
