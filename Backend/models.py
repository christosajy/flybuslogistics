from django.db import models

# Create your models here.

class ModeDB(models.Model):
    ModeName = models.CharField(max_length=50, null=True, blank=True)
    ModeDesc = models.TextField( null=True, blank=True)
    ModeDesc_P1 = models.TextField( null=True, blank=True)
    ModeDesc_P2 = models.TextField( null=True, blank=True)
    ModeDesc_P3 = models.TextField( null=True, blank=True)
    ModeDesc_P4 = models.TextField( null=True, blank=True)
    ModeDesc_P5 = models.TextField( null=True, blank=True)
    ModeImage = models.ImageField(upload_to='ICNS', null=True, blank=True)

class TypeDB(models.Model):
    TypeName = models.CharField(max_length=50, null=True, blank=True)
    TypeDesc = models.TextField(null=True, blank=True)    
    TypeDesc_P1 = models.TextField(null=True, blank=True)    
    TypeDesc_P2 = models.TextField(null=True, blank=True)    
    TypeDesc_P3 = models.TextField(null=True, blank=True)    
    TypeDesc_P4 = models.TextField(null=True, blank=True)    
    TypeDesc_P5 = models.TextField(null=True, blank=True)    

class VideoDb(models.Model):
    HomeVideo = models.FileField(upload_to='videos', null=True, blank=True)

class AddressDb(models.Model):
    Email = models.CharField(max_length=100, null=True, blank=True)    
    Website = models.CharField(max_length=100, null=True, blank=True)    
    Address = models.TextField(null=True, blank=True)    
    ContactNum = models.CharField(max_length=100, null=True, blank=True)     
    Copy_right = models.CharField(max_length=100, null=True, blank=True)     

class TeamDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)    
    Designation = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to='team', null=True, blank=True)    
    Social_1 = models.CharField(max_length=100, null=True, blank=True)    
    Social_2 = models.CharField(max_length=100, null=True, blank=True)    
    Social_3 = models.CharField(max_length=100, null=True, blank=True)    
    Social_4 = models.CharField(max_length=100, null=True, blank=True)    

class LocationDb(models.Model):   
    Hub = models.CharField(max_length=100, null=True, blank=True) 
    Location = models.TextField(null=True, blank=True)   