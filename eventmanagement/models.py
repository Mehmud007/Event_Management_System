from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phnno = models.IntegerField()
    def __str__(self):
        return self.firstname

class Cateror(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phnno = models.IntegerField()
    def __str__(self):
        return self.firstname

class Decorator(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phnno = models.IntegerField()
    def __str__(self):
        return self.firstname
        
class Hall(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    hall_capacity = models.IntegerField()
    address = models.CharField(max_length=400)
    hall_description = models.TextField()
    hall_rent = models.FloatField()
    is_booked = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Event(models.Model):
    customer_name = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    phnno = models.IntegerField()
    event_type = models.CharField(max_length=200)
    starting_date = models.DateField()
    ending_date = models.DateField()
    event_time = models.TimeField()
    no_of_persons = models.IntegerField()
    selected_package = models.CharField(max_length=200)
    selected_hall = models.CharField(max_length=200)
    selected_cateror = models.CharField(max_length=200, default="Not selected")
    selected_decorator = models.CharField(max_length=200, default="Not selected")
    total_amount = models.FloatField()
    def __str__(self):
        return self.event_type    

class Event_Type(models.Model):
    Event_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Event_name

class Package(models.Model):
    Package_name = models.CharField(max_length=200)
    Price_per_person = models.FloatField()

    def __str__(self):
        return self.Package_name

class Wedding_Package(models.Model):
    Package_name = models.CharField(max_length=200)
    person_capacity = models.IntegerField()
    package_price = models.FloatField()
    Price_per_extra_day = models.FloatField()
    Price_per_extra_fifty_person = models.FloatField()
    No_of_days = models.IntegerField()

    def __str__(self):
        return self.Package_name   

class Corporate_Package(models.Model):
    Package_name = models.CharField(max_length=200)
    person_capacity = models.IntegerField()
    package_price = models.FloatField()
    Price_per_extra_day = models.FloatField()
    Price_per_extra_fifty_person = models.FloatField()
    No_of_days = models.IntegerField()

    def __str__(self):
        return self.Package_name    