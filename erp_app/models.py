from datetime import date
from django.db import models
from localflavor.us.models import USStateField

# Create your models here.


class Driver(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    license_number = models.CharField(max_length=45)
    license_state = USStateField()
    license_exp_date = models.DateField()
    driver_start_date = models.DateField(
        default=date(2025, 1, 1), verbose_name="Hire date"
    )
    driver_end_date = models.DateField(
        null=True, blank=True, verbose_name="Termination date"
    )
    driver_active = models.BooleanField(default=False, blank=True)


class Truck(models.Model):
    truck_number = models.CharField(max_length=45)
    truck_vin_number = models.CharField(max_length=45)
    truck_year = models.CharField(max_length=45)
    truck_make = models.CharField(max_length=45)
    truck_plate_number = models.CharField(max_length=45)
    truck_plate_state = USStateField()
    truck_start_date = models.DateField(default=date(2025, 1, 1))
    truck_end_date = models.DateField(
        null=True, blank=True, verbose_name="Termination date"
    )
    truck_active = models.BooleanField(default=False, blank=True)


class Trailer(models.Model):
    trailer_number = models.CharField(max_length=45)
    trailer_vin_number = models.CharField(max_length=45)
    trailer_year = models.CharField(max_length=45)
    trailer_make = models.CharField(max_length=45)
    trailer_plate_number = models.CharField(max_length=45)
    trailer_plate_state = USStateField()
    trailer_start_date = models.DateField(default=date(2025, 1, 1))
    trailer_end_date = models.DateField(
        null=True, blank=True, verbose_name="Termination date"
    )
    truck_active = models.BooleanField(default=False, blank=True)


class Load(models.Model):
    load_number = models.CharField(max_length=45)
    location_pickup = models.CharField(max_length=45)
    location_delivery = models.CharField(max_length=45)
    pickup_date = models.DateField()
    delivery_date = models.DateField(null=True, blank=True)
    total_cost = models.IntegerField()
    load_status_delivered = models.BooleanField(default=False, blank=True)
    driver = models.ForeignKey("Driver", on_delete=models.CASCADE)
    # If driver deleted do not delete the load
    # driver = models.ForeignKey("Driver", on_delete=models.SET_NULL, null=True)


class Payroll(models.Model):
    payroll_date = models.DateField()
    total_pay = models.IntegerField()
    driver = models.ForeignKey("Driver", on_delete=models.CASCADE)
    # If driver deleted do not delete the payrol
    # driver = models.ForeignKey("Driver", on_delete=models.SET_NULL, null=True)
