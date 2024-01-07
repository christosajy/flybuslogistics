from django.db import models
# Create your models here.

class TrackingDb(models.Model):
    TrackingID = models.IntegerField(null=True, blank=True)
    WarehouseID = models.IntegerField(null=True, blank=True)

class QuoteDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)

class ContactUsDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Proffession = models.CharField(max_length=255, null=True, blank=True)
    Message = models.TextField(null=True, blank=True)

class SignupDb(models.Model):  
    Full_Name = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.CharField(max_length=100, null=True, blank=True)
    Address = models.TextField(null=True, blank=True)
    Locality = models.CharField(max_length=100, null=True, blank=True)  
    Proffession = models.CharField(max_length=100, null=True, blank=True)  
    Pincode = models.CharField(max_length=100, null=True, blank=True)  
    State = models.CharField(max_length=100, null=True, blank=True)  
    Country = models.CharField(max_length=100, null=True, blank=True)  
    Email = models.CharField(max_length=100, null=True, blank=True)  
    Password = models.CharField(max_length=100, null=True, blank=True)
    ProImg = models.ImageField(upload_to='profile', null=True, blank=True)

class ShipDb(models.Model):
    Shipping_ID = models.CharField(max_length=100, null=True, blank=True)
    From_Address = models.CharField(max_length=100, null=True, blank=True)
    To_Address = models.CharField(max_length=100, null=True, blank=True)
    Dep_Date = models.CharField(max_length=100, null=True, blank=True)
    Est_Del_Date = models.CharField(max_length=100, null=True, blank=True)
    Class = models.CharField(max_length=100, null=True, blank=True)
    Volume = models.CharField(max_length=100, null=True, blank=True)
    Type = models.CharField(max_length=100, null=True, blank=True)
    Order_Status = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)

class WarehouseDb(models.Model):
    Warehouse_ID = models.CharField(max_length=100, null=True, blank=True)
    StartDate = models.CharField(max_length=100, null=True, blank=True)    
    EndDate = models.CharField(max_length=100, null=True, blank=True)    
    Type = models.CharField(max_length=100, null=True, blank=True)
    Hub = models.CharField(max_length=100, null=True, blank=True)
    Order_Status = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)

class OrderStorage(models.Model):
    Order_Status = models.CharField(max_length=100, null=True, blank=True)   

class WeightStorage(models.Model): 
    Weightage = models.CharField(max_length=100, null=True, blank=True)    

class ClassStorage(models.Model):
    Class = models.CharField(max_length=100, null=True, blank=True)    
    
# class TestimonaialsDb(models.Model):
#     ProfilePic = models.ImageField(upload_to='Testimonials', null=True, blank=True)
#     Name = models.CharField(max_length=255, null=True, blank=True)
#     Proffession = models.CharField(max_length=255, null=True, blank=True)
#     Testimonial = models.TextField(null=True, blank=True)
#     Email = models.CharField(max_length=100, null=True, blank=True)

class MainbodyDb(models.Model):
    Top_Heading = models.CharField(max_length=255, null=True, blank=True) 
    Main_Heading = models.CharField(max_length=255, null=True, blank=True) 
    Sub_Heading = models.CharField(max_length=255, null=True, blank=True)
    Content_P1 = models.TextField(null=True, blank=True) 
    Content_P2 = models.TextField(null=True, blank=True) 
    Content_P3 = models.TextField(null=True, blank=True) 
    Content_P4 = models.TextField(null=True, blank=True) 
    Content_P5 = models.TextField(null=True, blank=True) 
   