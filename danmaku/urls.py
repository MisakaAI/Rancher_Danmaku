from django.urls import path

from . import views

urlpatterns = [
    path('', views.ranklist, name='index'),
    path('ranklist/', views.ranklist, name='index'),
    path('id/<str:name>', views.name, name='name'),
    path('documentation/', views.documentation, name='documentation'),
    path('about/', views.about, name='about'),
    path('danmaku/', views.danmaku, name='danmaku'),
]