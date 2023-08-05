"""
URL configuration for fusion project.

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
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

'''
urlpatterns =[
    path('admin/', projeto_vitor.urls),
    path('', include('core.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.index_title = 'Projeto Vitor'
admin.site.site_header = 'Administração do Projeto Django-Vitor'
admin.site.site_title = 'Administração Site'
