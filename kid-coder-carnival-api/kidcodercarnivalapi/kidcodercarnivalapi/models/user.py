# The above classes define a custom user model and manager in Django with specific methods for
# creating users and superusers.
# `from django.db import models` is importing the `models` module from the Django package in Python.
# This module provides a set of classes and functions that allow developers to define data models for
# their Django applications. The `models` module is commonly used to create database tables, fields,
# relationships, and constraints by defining Python classes that represent these database structures.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework.authtoken.models import Token

# This class likely represents a user model that extends AbstractUser in a Python application.
class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('kid', 'Kid'),
    )

    role = models.CharField(max_length=10, choices=ROLES, default='kid')
    last_login = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'users'  # This sets the table name to 'users'
