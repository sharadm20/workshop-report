# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ElsiClgContactDtl(models.Model):
    clg_id = models.IntegerField()
    name = models.CharField(max_length=512, blank=True, null=True)
    emailid = models.CharField(max_length=256, blank=True, null=True)
    gender = models.CharField(max_length=12, blank=True, null=True)
    branch = models.CharField(max_length=128, blank=True, null=True)
    alt_email1 = models.CharField(max_length=256, blank=True, null=True)
    alt_email2 = models.CharField(max_length=256, blank=True, null=True)
    alt_email3 = models.CharField(max_length=256, blank=True, null=True)
    contact_num = models.CharField(max_length=50, blank=True, null=True)
    alt_contact1 = models.CharField(max_length=50, blank=True, null=True)
    alt_contact2 = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(db_column='Active', max_length=50, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(max_length=256, blank=True, null=True)
    type = models.IntegerField()
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    status_cnt = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_clg_contact_dtl'


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


class ElsiDepartments(models.Model):
    name = models.CharField(max_length=512)
    main_branch = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_departments'


class ElsiDesignations(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_designations'


class ElsiRegion(models.Model):
    region_name = models.CharField(max_length=512)
    type = models.IntegerField()
    active = models.IntegerField()
    clg_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_region'


class ElsiState(models.Model):
    code = models.CharField(max_length=6, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_state'


class ElsiTeachersDtls(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    emailid = models.CharField(max_length=256, blank=True, null=True)
    alt_email1 = models.CharField(max_length=256, blank=True, null=True)
    alt_email2 = models.CharField(max_length=256, blank=True, null=True)
    contact_num = models.CharField(max_length=25, blank=True, null=True)
    alt_contact1 = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=128, blank=True, null=True)
    designation = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    coor_flag = models.IntegerField()
    wo_flag = models.IntegerField()
    workshop_id = models.IntegerField()
    wo_attendee = models.IntegerField()
    wo_count = models.IntegerField()
    eyrtc_flag = models.IntegerField()
    tbt_flag = models.IntegerField()
    eyic_flag = models.IntegerField()
    content_flag = models.IntegerField(blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=150, blank=True, null=True)  # Field name made lowercase.
    status_flag = models.IntegerField(blank=True, null=True)
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    elsi_flag = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    login_created = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elsi_teachers_dtls'


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


class WorkshopParticipants(models.Model):
    workshop_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    tch_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workshop_participants'


class WorkshopShipmentDtls(models.Model):
    workshop_id = models.IntegerField(blank=True, null=True)
    clg_id = models.IntegerField(blank=True, null=True)
    shipment_date = models.DateField(blank=True, null=True)
    tracking_no = models.IntegerField(blank=True, null=True)
    mode_of_dispatch = models.CharField(max_length=1024, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'workshop_shipment_dtls'


class WorkshopTeam(models.Model):
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workshop_team'


class WorkshopHospitality(models.Model):
    workshop_id = models.IntegerField(blank=True, null=True)
    hospitality = models.TextField(null=True)
    quality_accommodation = models.TextField(null=True)
    quality_food = models.TextField(null=True)
    quality_logistics = models.TextField(null=True)
    observation = models.TextField(null=True)
    expenditure = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'workshop_hospitality'
