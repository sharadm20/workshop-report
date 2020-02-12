from django.conf import settings
import os
import json
import matplotlib.pyplot as plt
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.db.models import Count, Case, When, DecimalField
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
import numpy as np
from .forms import WorkshopConductedForm, WorkshopModulesForm
from .forms import WorkshopHospitalityForm
from .models import *
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile


def index(request):
    return render(request, 'generatePdf/pages/index.html')


def generatedReports(request):
    reports = WorkshopConductedData.objects.order_by('-created_at').all()
    return render(request, 'generatePdf/pages/old_reports.html', {'reports': reports})


def stepOne(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WorkshopConductedForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            workshop = WorkshopDtls.objects.select_related('clg').get(id=form.cleaned_data['workshop_id'])
            workshop_conducted = form.save()

            workshop_conducted.clg_id = workshop.clg_id
            workshop_conducted.college_name = workshop.clg.college_name
            workshop_conducted.save()  # update college id and name
            request.session['workshop_detail'] = workshop_conducted
            return redirect('step2')
        else:
            return render(request, 'generatePdf/pages/form_step_1.html', {'form': form})

        # if a GET (or any other method) we'll create a blank form
    else:
        form = WorkshopConductedForm()
        return render(request, 'generatePdf/pages/form_step_1.html', {'form': form})


def stepTwo(request):
    if request.method == 'POST' and request.FILES['report_file']:
        report_file = request.FILES['report_file']
        fs = FileSystemStorage()
        if request.session['workshop_detail']:
            filename = fs.save(request.session['workshop_detail']['id'] + "_report.csv", report_file)
        else:
            filename = fs.save('report.csv', report_file)
        uploaded_file_url = fs.url(filename)
        request.session['uploaded_file_url'] = uploaded_file_url
        form = WorkshopModulesForm(request.POST)
        if form.is_valid():
            return redirect('step3')
        else:
            return render(request, 'generatePdf/pages/form_step_2.html', {'form': form})
    else:
        if request.session['workshop_detail']:
            form = WorkshopModulesForm()
            return render(request, 'generatePdf/pages/form_step_2.html', {'form': form})
        else:
            request.session.flush()
            return redirect('step1')


def stepThree(request):
    if request.method == 'POST':
        form = WorkshopHospitalityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('step4')
        else:
            return render(request,
                          'generatePdf/pages/form_step_3.html',
                          {'form': form})
    else:
        if request.session['workshop_detail']:
            try:
                hospitality_form = WorkshopHospitality.objects.get(workshop_id=request.session
                ['workshop_detail']['workshop_id'])
                form = WorkshopHospitalityForm(hospitality_form)
                return render(request, 'generatePdf/pages/form_step_3.html', {'form': form})
            except WorkshopHospitality.DoesNotExist:
                form = WorkshopHospitalityForm()
                return render(request, 'generatePdf/pages/form_step_3.html', {'form': form})
        else:
            request.seesion.flush()
            return redirect('step1')


def stepFour(request):
    if request.method == 'POST':
        if 'html' in request.POST:
            workshop = WorkshopConductedData.objects.get(workshop_id=request.session
            ['workshop_detail']['workshop_id'])
            return render(request, 'generatePdf/pages/form_as_html.html',
                          {'workshop': workshop
                           })
        elif 'pdf' in request.POST:
            return None
        else:
            return None
    else:
        if request.session['workshop_detail']:
            return render(request, 'generatePdf/pages/form_step_4.html')
        else:
            request.session.flush()
            return redirect('step1')


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
    workshop_id = request.session['workshop_detail']['workshop_id']
    data = {
        "workshop_id": workshop_id
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def workshopPdfHtml(request, workshop_id=None):
    if request.method == 'POST' and workshop_id is not None:
        context = get_context(workshop_id)
        return render(request, 'generatePdf/pages/form_as_html.html', context)


def workshopPdfDownload(request, workshop_id=None):
    if request.method == 'POST' and workshop_id is not None:
        context = get_context(workshop_id)
        html_string = render_to_string('generatePdf/pages/form_as_html.html', context)
        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        result = html.write_pdf()

        # Creating http response
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename=list_people.pdf'
        response['Content-Transfer-Encoding'] = 'binary'
        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output = open(output.name, 'rb')
            response.write(output.read())

        return response


def chartData(request):
    df = pd.read_csv('media/report.csv')
    df.columns = ['time', 'venue', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
                  'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'name',
                  'college', 'email']
    data = df.to_json()
    return JsonResponse(data)


def get_context(workshop_id):
    workshop_conducted = WorkshopConductedData.objects.get(id=workshop_id)
    workshop_hospitality = WorkshopHospitality.objects.get(workshop_conducted=workshop_id)
    workshop_modules = WorkshopModules.objects.get(workshop_conducted=workshop_id)
    workshop_feedback = WorkshopFeedbackResponse.objects.filter(workshop_conducted=workshop_id)
    plot_graph_save(workshop_feedback)
    context = {
        'workshop': workshop_conducted,
        'workshop_hospitality': workshop_hospitality,
        'workshop_modules': workshop_modules,
        'data': workshop_feedback,
        'count': workshop_feedback.count(),
    }
    return context


def plot_graph_save(workshop_feedback):
    q1_count = workshop_feedback.values('q1').annotate(count=Count('q1'))
    sizes = [item['count'] for item in q1_count]
    labels = [tag.value for tag in Q1Choice]
    filename = 'generatePdf/static/generatePdf/img/q1.png'

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(os.path.join(settings.BASE_DIR, filename))
    q2_count = workshop_feedback.values('q2').annotate(count=Count('q2'))
    filename = 'generatePdf/static/generatePdf/img/q2.png'
    labels = [tag.value for tag in Q2Choice]
    sizes = [item['count'] for item in q2_count]
    fig2, ax2 = plt.subplots()
    ax2.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax2.axis('equal')
    plt.savefig(os.path.join(settings.BASE_DIR, filename))
    q7_count = workshop_feedback.values('q7').annotate(count=Count('q7')).order_by('q7')
    filename = 'generatePdf/static/generatePdf/img/q7.png'
    objects = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    indexZ = np.arange(len(objects))
    performance = [item['count'] for item in q7_count]
    print(performance)
    plt.bar(indexZ, performance)
    plt.xticks(indexZ, objects)
    plt.ylabel('Ratings')
    plt.title('Introduction')
    plt.savefig(os.path.join(settings.BASE_DIR, filename))