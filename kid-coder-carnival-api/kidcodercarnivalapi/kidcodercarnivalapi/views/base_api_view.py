# views.py
from django.views.generic import View
from django.http import JsonResponse

# Base view class
class BaseAPIView(View):
    def __init__(self):
        pass
