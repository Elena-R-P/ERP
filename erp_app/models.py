from datetime import date
from django.db import models
from localflavor.us.models import USStateField
from django.core.validators import MinLengthValidator
from django.db.models import Sum

# Create your models here.


class Driver(models.Model):
    first_name = models.CharField(max_length=45, verbose_name="First Name")
    last_name = models.CharField(max_length=45, verbose_name="Last Name")
    date_of_birth = models.DateField(verbose_name="Date of birth")
    license_number = models.CharField(max_length=45, verbose_name="CDL #")
    license_state = USStateField(verbose_name="State")
    license_exp_date = models.DateField(verbose_name="CDL exp date")
    driver_start_date = models.DateField(
        default=date(2025, 1, 1), verbose_name="Hire date"
    )
    driver_end_date = models.DateField(
        null=True, blank=True, verbose_name="Termination date"
    )
    driver_active = models.BooleanField(
        default=False, blank=True, verbose_name="Driver active"
    )

    # Shows up in the admin list
    def __str__(self):
        return self.first_name


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

    # Shows up in the admin list
    def __str__(self):
        return self.truck_number


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

    # Shows up in the admin list
    def __str__(self):
        return self.trailer_number


class Load(models.Model):
    load_number = models.CharField(max_length=45)
    location_pickup = models.CharField(max_length=45)
    location_delivery = models.CharField(max_length=45)
    pickup_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField(null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    # payroll = models.ForeignKey(
    #    "Payroll", on_delete=models.CASCADE, null=True, blank=True
    # )
    # If driver deleted do not delete the load
    # driver = models.ForeignKey("Driver", on_delete=models.SET_NULL, null=True)

    # Shows up in the admin list
    def __str__(self):
        return self.load_number


"""
class Payroll(models.Model):
    payroll_date = models.DateField(auto_now_add=True)
    # total_pay = models.IntegerField() - will be calculated
    discount_percentage = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0
    )
    driver = models.ForeignKey("Driver", on_delete=models.CASCADE)
    load = models.ForeignKey(Load, on_delete=models.CASCADE)
    # add related name, connect with
    # If driver deleted do not delete the payrol
    # driver = models.ForeignKey("Driver", on_delete=models.SET_NULL, null=True)

    @property
    # Payroll Calculations
    def calculate_driver_payrol(self, driver_id, year, month):
        driver = Driver.objects.get(id=driver_id)

        # Filter loads by driver and month/year
        driver_loads = Load.objects.filter(
            driver=driver, delivery_date__year=year, delivery_date__month=month
        )

        # Calculate total pay for the specific period
        total_pay = driver_loads.aggregate(Sum("total_cost"))["total_cost__sum"]

        ctx = {"driver": driver, "year": year, "month": month, "total_pay": total_pay}
"""
