from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form-page-1', views.formPageOne, name="form1"),
    path('workshop_dtls', views.workshopDtls, name="workshop"),
]
