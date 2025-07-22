from django.forms import ModelForm
from .models import Driver, Truck, Trailer, Load, Payroll


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

