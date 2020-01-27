from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('step-2', views.stepTwo, name="step2"),
    path('step-3', views.stepThree, name="step3"),
    path('ajax/workshop_dtls', views.workshopDtls, name="workshop"),
    path('ajax/workshop_id', views.workshopId, name="workshop_id"),
]
