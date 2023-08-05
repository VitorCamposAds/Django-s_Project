from django.urls import path
from.views import IndexView
from django.contrib import admin



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

admin.site.index_title = 'Projeto Vitor'
admin.site.site_header = 'Administração do Projeto'
admin.site.site_title = 'Administração Site'