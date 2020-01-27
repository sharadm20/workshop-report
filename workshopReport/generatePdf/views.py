from django.core import serializers
from django.http import HttpResponse
import json
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.forms import ValidationError
from django.core.files.storage import FileSystemStorage
from .forms import WorkshopDtlsForm
from .forms import WorkshopHospitalityForm
from .models import *


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print(request.POST)
        form = WorkshopDtlsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('inside:')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            request.session['workshop_detail'] = request.POST
            return render(request, 'generatePdf/pages/form_step_2.html')
        else:
            return render(request, 'generatePdf/pages/form_step_1.html', {'form': form})

        # if a GET (or any other method) we'll create a blank form
    else:
        form = WorkshopDtlsForm()
        return render(request, 'generatePdf/pages/form_step_1.html', {'form': form})


def stepTwo(request):
    if request.method == 'POST' and request.FILES['report_file']:
        report_file = request.FILES['report_file']
        fs = FileSystemStorage()
        filename = fs.save("report.csv", report_file)
        uploaded_file_url = fs.url(filename)
        request.session['uploaded_file_url'] = uploaded_file_url
        form = WorkshopHospitalityForm()
        return render(request, 'generatePdf/pages/form_step_3.html', {
            'uploaded_file_url': uploaded_file_url,
            'form': form
        })
    else:
        if request.session['workshop_detail']:
            return render(request, 'generatePdf/pages/form_step_2.html')
        else:
            return redirect('/')


def stepThree(request):
    if request.method == 'POST':
        form = WorkshopHospitalityForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'generatePdf/pages/form_step_4.html')
    else:
        form = WorkshopHospitalityForm()
        return render(request, 'generatePdf/pages/form_step_3.html', {'form': form})


def workshopDtls(request):
    clg_id = request.POST['clg_id']
    workshop = WorkshopDtls.objects.get(id=clg_id)
    data = {
        "start_date": str(workshop.start_date),
        "end_date": str(workshop.end_date),
        "workshop_team": str(workshop.workshop_team)
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def workshopId(request):
    workshop = request.session['workshop_detail']
    data = {
        "workshop_id": workshop.workshop_id
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
