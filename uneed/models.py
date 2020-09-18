from django.db import models

# Create your models here.
class Tbl_user(models.Model):
    u_name=models.CharField(max_length=255, null=True)
    u_password=models.CharField(max_length=255, null=True)
    u_email=models.CharField(max_length=255, null=True)
    u_phno=models.CharField(max_length=255, null=True)
    u_address=models.CharField(max_length=255, null=True)
    u_gst=models.CharField(max_length=255, null=True)
    u_panno=models.CharField(max_length=255, null=True)
    u_servicetaxno=models.CharField(max_length=255, null=True)
    u_documents=models.ImageField(upload_to='images/', null=True)
    u_role=models.CharField(max_length=255, null=True)
    u_status=models.CharField(max_length=255, null=True)
    u_token=models.CharField(max_length=255, null=True)
    u_otp=models.IntegerField(null=True)
    u_otp_is_used=models.IntegerField( null=True)
    u_createddate=models.DateTimeField(auto_now=True)
    u_modifieddate=models.DateTimeField(auto_now=True)
    u_createdby=models.IntegerField(null=True)
    u_modifiedby=models.IntegerField(null=True)