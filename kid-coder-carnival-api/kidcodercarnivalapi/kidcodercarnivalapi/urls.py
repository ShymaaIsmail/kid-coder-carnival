# The code snippet you provided is a URL configuration for a Django project named
# `kidcodercarnivalapi`. In Django, the `urlpatterns` list is used to route URLs to views within the
# project.
"""
URL configuration for kidcodercarnivalapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Create schema view instance
schema_view = get_schema_view(
    openapi.Info(
        title="Kid Coder Carnival API",
        default_version='v1',
        extra="Shymaa M. Ismail",
        description="Kid Coder Carnival API description",
        terms_of_service="https://www.shymaaismai.tech",
        contact=openapi.Contact(email="shymaa.m.ismail@gmail.com"),
        license=openapi.License(name="Shymaa Mohamed Ismail -ALX SWE Program- Cohort 18"),
    ),
    public=True,
    url='https://shymaaismail.tech/kids-coder-api/',  # This sets the base URL for the API

)


urlpatterns = [
    # Admin APIs
    path('admin/', admin.site.urls),
    path('auth/', include('kidcodercarnivalapi.api_urls.auth_urls')),
    path('profile/', include('kidcodercarnivalapi.api_urls.profile_urls')),
    path('competitions/', include('kidcodercarnivalapi.api_urls.competitions_urls')),
    path('challenges/', include('kidcodercarnivalapi.api_urls.challenges_urls')),
    # Kids APIs
    path('kids/', include('kidcodercarnivalapi.api_urls.kids_competitions_urls')),
    # Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
