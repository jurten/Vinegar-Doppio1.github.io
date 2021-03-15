"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pages.views import home_page, contact_us_page, turn_page, faq_page
from turn.views import turn_detailed_view

urlpatterns = [
    path("", home_page, name="home"),
    path("turnos/", turn_page, name="turn page"),
    path("contacto/", contact_us_page, name="contact us"),
    path("detalles_turnos/", turn_detailed_view, name="turn detail"),
    path("preguntas_frecuentes/", faq_page, name="FAQ page"),
    path("admin/", admin.site.urls),
]
