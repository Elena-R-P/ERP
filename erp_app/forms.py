from django import forms
from django.forms import ModelForm, widgets
from .models import Driver, Payroll, Truck, Trailer, Load


# Create the form class
class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = "__all__"
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "license_exp_date": forms.DateInput(attrs={"type": "date"}),
            "driver_start_date": forms.DateInput(attrs={"type": "date"}),
            "driver_end_date": forms.DateInput(attrs={"type": "date"}),
        }


class TruckForm(ModelForm):
    class Meta:
        model = Truck
        fields = "__all__"
        widgets = {
            "truck_start_date": forms.DateInput(attrs={"type": "date"}),
            "truck_end_date": forms.DateInput(attrs={"type": "date"}),
        }


class TrailerForm(ModelForm):
    class Meta:
        model = Trailer
        fields = "__all__"
        widgets = {
            "trailer_start_date": forms.DateInput(attrs={"type": "date"}),
            "trailer_end_date": forms.DateInput(attrs={"type": "date"}),
        }


class LoadForm(ModelForm):
    class Meta:
        model = Load
        fields = "__all__"
        widgets = {
            "pickup_date": forms.DateInput(attrs={"type": "date"}),
            "delivery_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        driver_id = kwargs.pop("driver_id", None)
        super().__init__(*args, **kwargs)
        if driver_id:
            self.fields["driver"].initial = Driver.objects.get(id=driver_id)


class PayrollForm(ModelForm):
    class Meta:
        model = Payroll
        fields = "__all__"
        widgets = {
            "payroll_date": forms.DateInput(attrs={"type": "date"}),
        }
