from django.core import serializers
from django.http import HttpResponse
import json
from django.shortcuts import render
from .models import *


def index(request):
    workshops = WorkshopDtls.objects.order_by('-start_date').all()
    return render(request, 'generatePdf/pages/report_form.html', {'workshops': workshops})


def formPageOne(request):
    print(request.POST)

    return render(request, 'generatePdf/pages/report_form.html')


def workshopDtls(request):
    clg_id = request.POST['clg_id']
    workshop = WorkshopDtls.objects.get(id=clg_id)
    data = {
        "start_date": str(workshop.start_date),
        "end_date": str(workshop.end_date),
        "workshop_team": str(workshop.workshop_team)
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
