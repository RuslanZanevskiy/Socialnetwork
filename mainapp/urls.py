from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.index, name='homepage'),
    path('', views.default_redirect_view),
]
