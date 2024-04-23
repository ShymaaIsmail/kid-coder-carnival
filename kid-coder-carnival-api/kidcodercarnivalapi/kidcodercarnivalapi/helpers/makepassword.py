#!/usr/bin/env python3
from django.contrib.auth.hashers import make_password
password = 'admin'
hashed_password = make_password(password)

print(hashed_password)
