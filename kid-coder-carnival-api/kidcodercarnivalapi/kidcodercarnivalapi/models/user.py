# `from django.db import models` is importing the `models` module from the Django package in Python.
# This module provides a set of classes and functions that allow developers to define data models for
# their Django applications. The `models` module is commonly used to create database tables, fields,
# relationships, and constraints by defining Python classes that represent these database structures.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# This class is a custom user manager class that likely handles user creation and management in a
# Python application.


class UserManager(BaseUserManager):
    def create_user(self, fullname, email, password=None, role=None, **extra_fields):
        """
        The function creates a user with specified details like full name, email, password, and role in
        Python.

        :param fullname: The `fullname` parameter in the `create_user` method represents the full name
        of the user being created. It is a required field that must be provided when creating a new user
        :param email: The `email` parameter is a required field for creating a user. If the `email`
        field is not provided, a `ValueError` will be raised with the message 'The Email field must be
        set'. The `email` field is also normalized using the `normalize_email` method before creating
        :param password: The `password` parameter in the `create_user` method is used to set the
        password for the user being created. It is optional and defaults to `None`, which means that if
        a password is not provided when calling the method, the user will be created without a password
        :param role: The `role` parameter in the `create_user` method is used to specify the role of the
        user being created. It is an optional parameter that allows you to assign a specific role to the
        user during the creation process. If no role is provided, the user will be created without a
        specific role
        :return: The `create_user` method returns the user object that has been created and saved in the
        database.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(fullname=fullname, email=email,
                          role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, fullname, email, password=None, role='admin', **extra_fields):
        """
        The function `create_superuser` creates a superuser with specific attributes in a Python class.

        :param fullname: fullname is a parameter that represents the full name of the user for whom the
        superuser account is being created
        :param email: The `create_superuser` method is a custom method for creating a superuser in a
        Django application. It takes several parameters including `fullname`, `email`, `password`,
        `role`, and additional `extra_fields`
        :param password: The `password` parameter in the `create_superuser` method is used to set the
        password for the superuser being created. It is an optional parameter, meaning that if no
        password is provided, the superuser can be created without a password
        :param role: The `role` parameter in the `create_superuser` function is a string that specifies
        the role of the user being created. By default, it is set to 'admin', but you can provide a
        different role if needed, defaults to admin (optional)
        :return: The `create_superuser` method is returning the result of calling the `create_user`
        method with the provided arguments and extra fields.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(fullname, email, password, role, **extra_fields)

# This class likely represents a user model that extends AbstractBaseUser in a Python application.


class User(AbstractBaseUser):
    ROLES = (
        ('admin', 'Admin'),
        ('kid', 'Kid'),
    )

    fullname = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLES, default='kid')
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'email']

    def __str__(self):
        """
        The above function is a Python special method that returns the `fullname` attribute as a string
        representation of the object.
        :return: The `fullname` attribute of the object is being returned as a string.
        """
        return self.fullname
