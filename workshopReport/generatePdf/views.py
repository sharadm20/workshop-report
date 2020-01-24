from django.core import serializers
from django.http import HttpResponse
import json
from django.shortcuts import render

from .forms import WorkshopDtlsForm
from .models import *


def index(request):
    workshops = WorkshopDtls.objects.order_by('-start_date').select_related('clg')
    form = WorkshopDtlsForm(workshops)
    return render(request, 'generatePdf/pages/form_step_1.html', {'form': form})


def formPageOne(request):
    request.session['workshop_detail'] = request.POST
    return render(request, 'generatePdf/pages/form_step_2.html')


def workshopDtls(request):
    clg_id = request.POST['clg_id']
    workshop = WorkshopDtls.objects.get(id=clg_id)
    data = {
        "start_date": str(workshop.start_date),
        "end_date": str(workshop.end_date),
        "workshop_team": str(workshop.workshop_team)
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
