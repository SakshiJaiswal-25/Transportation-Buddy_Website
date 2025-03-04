from django.db import models
from django.utils import timezone
# Create your models here.
# contact model
class Contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=30)
    message=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

#Scheme_Offers  model

class Scheme_Offers(models.Model):
    contents=models.CharField(max_length=45)
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.contents

#Feedback model

class FeedBack_Rating(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    feedback_text=models.TextField()
    ratings=models.CharField(max_length=6)
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

gender=[
    ("M","Male"),
    ("F","Female"),
]

#Employee model
class Employee(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    phone=models.CharField(max_length=10)
    designation=models.CharField(max_length=20)
    experience=models.CharField(max_length=10)
    gender=models.CharField(max_length=6,choices=gender)
    employee_pic=models.FileField(max_length=200,upload_to="transportapp/employee_pic",default="")

    def __str__(self):
        return self.name

#Vehicle model
class vehicle_manage(models.Model):
    truck_type=models.CharField(max_length=50)
    truck_size=models.CharField(max_length=40)
    truck_capacity=models.CharField(max_length=40)
    truck_weight=models.CharField(max_length=30)
    photo=models.FileField(max_length=200,upload_to="transportapp/truck_pic",default="")
    def __str__(self):
        return self.truck_type  
    
class customer_signup(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField(max_length=60)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.fname

class check_fare(models.Model):
    pick_up=models.CharField(max_length=100)
    drop=models.CharField(max_length=100)
    distance=models.CharField(max_length=5)
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.pick_up
    
class user_message(models.Model):
    sender_id=models.CharField(max_length=40)
    receiver_id=models.CharField(max_length=40)
    subject=models.CharField(max_length=40)
    message=models.CharField(max_length=100)
    sender_status=models.CharField(max_length=40,default="False")
    receiver_status=models.CharField(max_length=40,default="False")
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.sender_id




class Goods_type(models.Model):
    type=models.CharField(max_length=50)
    def __str__(self):
        return self.type

class Vehicle_booking(models.Model):
    user_id=models.CharField(max_length=40,null=False)
    veh_id=models.CharField(max_length=5)
    driver_id=models.CharField(max_length=40)
    truck_type=models.CharField(max_length=50,null=False)
    pick=models.CharField(max_length=200)
    drop=models.CharField(max_length=200)
    item_type=models.CharField(max_length=40)
    delivery_date=models.CharField(max_length=10)
    booking_date=models.CharField(max_length=10)
    date=models.DateField(default=timezone.now)
    paid_amount=models.CharField(max_length=30)
    booking_status=models.BooleanField(default=False)
    def __str__(self):
        return self.user_id        


    