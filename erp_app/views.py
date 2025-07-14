from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse


# Create your views here.
# Render Home page
def index(request):
    return render(request, "erp_app/index.html")


# Drivers
# Render drivers page
def drivers_list(request):
    return render(request, "erp_app/drivers.html")


# Drivers list view
# class DriverListView(View):
#    def get(self, request):
# TODO:
# Make a database call
# Load all the driver's records, turn them into objects
# Get a list of those objects
# Pass entire list to the HTML template


def trucks_list(request):
    return render(request, "erp_app/trucks.html")


def trailers_list(request):
    return render(request, "erp_app/trailers.html")


def loads_list(request):
    return render(request, "erp_app/loads.html")


def payroll(request):
    return render(request, "erp_app/payroll.html")


def contacts_list(request):
    return render(request, "erp_app/contacts.html")


# PAYROLL
# Calculate payroll
# TODO
# Create a new instance of a payroll
# Select a dr
