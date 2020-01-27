from django import forms

from .models import WorkshopHospitality
from .workshop_choice import choices


class WorkshopDtlsForm(forms.Form):
    workshop_id = forms.ChoiceField(label='Workshop conducted',
                                    widget=forms.Select(attrs={"onChange": 'getWorkshopDateAndTeam()'}),
                                    choices=choices(),
                                    required=True)
    workshop_team = forms.CharField(label='Workshop team')
    workshop_date_start = forms.CharField(label='Workshop start date')
    workshop_date_end = forms.CharField(label='Workshop end date')
    participants = forms.IntegerField(label='No of participants', required=True)
    college_count = forms.IntegerField(label='No of college', required=True)
    loi_count = forms.IntegerField(label='No of Loi collected', required=True)
    refresher_count = forms.IntegerField(label='No of refresher college', required=True)
    kits_distributed = forms.IntegerField(label='No of kits given', required=True)
    kits_pending = forms.IntegerField(label='No of kits pending', required=True)
    certificates_distributed = forms.IntegerField(label='No of certificates given', required=True)
    certificates_pending = forms.IntegerField(label='No of certificates pending', required=True)


class WorkshopHospitalityForm(forms.ModelForm):
    class Meta:
        model = WorkshopHospitality
        fields = ['workshop_id', 'hospitality', 'quality_accommodation', 'quality_food', 'quality_logistics', 'observation', 'expenditure']

    workshop_id = forms.IntegerField(widget=forms.HiddenInput())
    hospitality = forms.CharField(label='Hospitality', widget=forms.Textarea(attrs={"rows": 5, "cols": 100}))
    quality_accommodation = forms.CharField(label='Quality of accommodation',
                                            widget=forms.Textarea(attrs={"rows": 5, "cols": 100}))
    quality_food = forms.CharField(label='Quality of food arranged (Breakfast, Lunch, Dinner)',
                                   widget=forms.Textarea(attrs={"rows": 5, "cols": 100}))
    quality_logistics = forms.CharField(label='Quality of logistics',
                                        widget=forms.Textarea(attrs={"rows": 5, "cols": 100}))
    observation = forms.CharField(label='Our observations', widget=forms.Textarea(attrs={"rows": 5, "cols": 100}))
    expenditure = forms.IntegerField(label='Total expenditure of team')
