# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from .enum import Q1Choice, Q2Choice


class ElsiCollegeDtls(models.Model):
    clg_code = models.CharField(max_length=512, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    workshop_id = models.IntegerField()
    college_name = models.CharField(max_length=1024)
    abbreviation = models.CharField(max_length=128, blank=True, null=True)
    district = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    state = models.CharField(max_length=512, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    college_type = models.CharField(max_length=256, blank=True, null=True)
    principal_meet = models.IntegerField()
    robots_given = models.IntegerField(blank=True, null=True)
    eyic_allowed = models.IntegerField()
    eyrtc_allowed = models.IntegerField()
    tbt_allowed = models.IntegerField()
    content_allowed = models.IntegerField()
    legal_docs = models.IntegerField(blank=True, null=True)
    legal_docs_remarks = models.CharField(max_length=1024, blank=True, null=True)
    loi_status = models.IntegerField()
    loi_format = models.IntegerField(blank=True, null=True)
    loi_remarks = models.CharField(max_length=1024, blank=True, null=True)
    po_status = models.IntegerField(blank=True, null=True)
    po_remark = models.CharField(max_length=1024, blank=True, null=True)
    wo_reg = models.IntegerField()
    wo_invite = models.IntegerField()
    wo_confirm = models.IntegerField()
    wo_attend = models.IntegerField()
    hardware_given = models.CharField(max_length=1024, blank=True, null=True)
    lab_inaugurated = models.IntegerField()
    phase = models.IntegerField()
    eys2016_invites = models.IntegerField()
    team_verify = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'elsi_master'
        managed = False
        db_table = 'elsi_college_dtls'


class WorkshopDtls(models.Model):
    region_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    workshop_team = models.CharField(max_length=520)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    clg = models.ForeignKey(ElsiCollegeDtls, on_delete=models.DO_NOTHING)

    class Meta:
        app_label = 'elsi_master'
        managed = False
        db_table = 'workshop_dtls'


class WorkshopConductedData(models.Model):
    workshop_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    college_name = models.CharField(max_length=520, blank=True, null=True)
    workshop_team = models.CharField(max_length=520)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    participants = models.IntegerField(blank=True, null=True)
    college_count = models.IntegerField(blank=True, null=True)
    loi_count = models.IntegerField(blank=True, null=True)
    refresher_count = models.IntegerField(blank=True, null=True)
    kits_distributed = models.IntegerField(blank=True, null=True)
    kits_pending = models.IntegerField(blank=True, null=True)
    certificates_distributed = models.IntegerField(blank=True, null=True)
    certificates_pending = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.college_name, self.start_date, self.end_date)

    class Meta:
        managed = True
        db_table = 'workshop_conducted_data'


class WorkshopHospitality(models.Model):
    workshop_conducted = models.ForeignKey(WorkshopConductedData, on_delete=models.CASCADE)
    hospitality = models.TextField(null=True)
    quality_accommodation = models.TextField(null=True)
    quality_food = models.TextField(null=True)
    quality_logistics = models.TextField(null=True)
    observation = models.TextField(null=True)
    expenditure = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'workshop_hospitality'


class WorkshopModules(models.Model):
    intro_speaker = models.CharField(max_length=520, null=True)
    io_speaker = models.CharField(max_length=520, null=True)
    motor_speaker = models.CharField(max_length=520, null=True)
    lcd_speaker = models.CharField(max_length=520, null=True)
    adc_speaker = models.CharField(max_length=520, null=True)
    pwm_speaker = models.CharField(max_length=520, null=True)
    interrupt_speaker = models.CharField(max_length=520, null=True)
    wlf_speaker = models.CharField(max_length=520, null=True)
    workshop_conducted = models.ForeignKey(WorkshopConductedData, on_delete=models.CASCADE)
    hosts = models.CharField(max_length=520, null=True)
    principal = models.CharField(max_length=520, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'workshop_modules_taken'


class WorkshopFeedbackResponse(models.Model):
    name = models.CharField(max_length=255, null=True)
    college_name = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=250, null=True)
    feedback_for_venue = models.TextField(null=True)
    workshop_conducted = models.ForeignKey(WorkshopConductedData, on_delete=models.CASCADE)
    q1 = models.CharField(max_length=100, null=True, choices=[(tag, tag.value) for tag in Q1Choice])
    q2 = models.CharField(max_length=100, null=True, choices=[(tag, tag.value) for tag in Q2Choice])
    q3 = models.CharField(max_length=100, null=True)
    q4 = models.CharField(max_length=100, null=True)
    q5 = models.CharField(max_length=100, null=True)
    q6 = models.CharField(max_length=100, null=True)
    q7 = models.CharField(max_length=100, null=True)
    q8 = models.CharField(max_length=100, null=True)
    q9 = models.CharField(max_length=100, null=True)
    q10 = models.CharField(max_length=100, null=True)
    q11 = models.CharField(max_length=100, null=True)
    q12 = models.CharField(max_length=100, null=True)
    q13 = models.CharField(max_length=100, null=True)
    q14 = models.CharField(max_length=100, null=True)
    q15 = models.CharField(max_length=100, null=True)
    q16 = models.CharField(max_length=100, null=True)
    q17 = models.CharField(max_length=100, null=True)
    q18 = models.CharField(max_length=100, null=True)
    q19 = models.CharField(max_length=100, null=True)
    q20 = models.CharField(max_length=100, null=True)
    q21 = models.CharField(max_length=100, null=True)
    q22 = models.CharField(max_length=100, null=True)
    q23 = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'workshop_feedback_response'


class WorkshopFeedbackQuestion(models.Model):
    question = models.CharField(max_length=600, null=True)
    option_1 = models.CharField(max_length=100, null=True)
    option_2 = models.CharField(max_length=100, null=True)
    option_3 = models.CharField(max_length=100, null=True)

    class Meta:
        managed = True
        db_table = 'workshop_feedback_questions'
