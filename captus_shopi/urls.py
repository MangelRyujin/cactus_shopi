"""
URL configuration for captus_shopi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include,re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 
from django.conf.urls.static import static
from rest_framework import permissions
from django.conf import settings
from django.views.static import serve



schema_view = get_schema_view(
    openapi.Info(
        title = "Cactus Shopi API",
        default_version = "version 1.0",
        description = "Documentacion publica de API de Cactus Shopi",
        terms_of_service = "https://www.google.com/policies/terms/",
        contact = openapi.Contact(email ="infmangel@gmail.com"),
        License = openapi.License(name = "BSD License"),     
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plants/', include('apps.cactus.api.routers')),
    path('cliente/', include('apps.pedido.api.routers')),
    re_path(r'^swagger(?P<format>\.json/\.yaml)$', schema_view.without_ui(cache_timeout=0), name = 'schema-json'),
    path('swagger/', schema_view.with_ui('swagger',cache_timeout=0), name = 'schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0), name = 'schema-swagger-redoc'),
    
]

urlpatterns+=[
    re_path(r'^media/(?P<path>.*)$',serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]
