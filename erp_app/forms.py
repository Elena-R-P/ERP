from django import forms
from django.forms import ModelForm, widgets
from .models import Driver, Payroll, Truck, Trailer, Load


# Create the form class
class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = "__all__"


class TruckForm(ModelForm):
    class Meta:
        model = Truck
        fields = "__all__"


class TrailerForm(ModelForm):
    class Meta:
        model = Trailer
        fields = "__all__"


class LoadForm(ModelForm):
    class Meta:
        model = Load
        fields = "__all__"

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
