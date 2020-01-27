from .models import *


def choices():
    workshops = WorkshopDtls.objects.order_by('-start_date').select_related('clg')
    return [(workshop.id, str(workshop.clg.college_name)) for workshop in workshops]
