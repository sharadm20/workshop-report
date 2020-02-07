from django.urls import path
from . import views
from wkhtmltopdf.views import PDFTemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('step-1', views.stepOne, name='step1'),
    path('step-2', views.stepTwo, name="step2"),
    path('step-3', views.stepThree, name="step3"),
    path('step-4', views.stepFour, name="step4"),
    path('ajax/workshop_dtls', views.workshopDtls, name="workshop"),
    path('ajax/workshop_id', views.workshopId, name="workshop_id"),
    path('workshop_pdf_html/<int:workshop_id>', views.workshopPdfHtml, name="workshop_pdf_view"),
    path('workshop_pdf/<int:workshop_id>', views.workshopPdfDownload, name="workshop_pdf_download"),
    path('generated', views.generatedReports, name="generated_reports"),
    path('pdf', PDFTemplateView.as_view(template_name='generatePdf/pages/form_as_html.html',
                                           filename='report.pdf'), name='pdf'),
]
