from django import forms


class WorkshopDtlsForm(forms.Form):

    def __init__(self, workshops, *args, **kwargs):
        super(WorkshopDtlsForm, self).__init__(*args, **kwargs)
        self.fields['workshop_id'] = forms.ChoiceField(
            choices=[(workshop.id, str(workshop.clg.college_name)) for workshop in workshops]
        )

    workshop_id = forms.ChoiceField(label='Workshop conducted', required=True)
    workshop_team = forms.CharField(label='Workshop team', disabled=True)
    workshop_date_start = forms.CharField(label='Workshop start date', disabled=True)
    workshop_date_end = forms.CharField(label='Workshop end date', disabled=True)
    participants = forms.IntegerField(label='No of participants', required=True)
    college_count = forms.IntegerField(label='No of college', required=True)
    loi_count = forms.IntegerField(label='No of Loi collected', required=True)
    refresher_count = forms.IntegerField(label='No of refresher college', required=True)
    kits_distributed = forms.IntegerField(label='No of kits given', required=True)
    kits_pending = forms.IntegerField(label='No of kits pending', required=True)
    certificates_distributed = forms.IntegerField(label='No of certificates given', required=True)
    certificates_pending = forms.IntegerField(label='No of certificates pending', required=True)
