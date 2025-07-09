from django.shortcuts import redirect, render


# Create your views here.
def index(request):
    return render(request, "erp_app/index.html")


def drivers_list(request):
    return render(request, "erp_app/drivers.html")


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
