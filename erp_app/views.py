#
# import {{{1
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.db.models import Sum

from .models import Driver, Payroll, Truck, Trailer, Load
from .forms import DriverForm, PayrollForm, TruckForm, TrailerForm, LoadForm

# }}}1


# Render Home page
def index(request):
    return render(request, "erp_app/index.html")


# DriverView {{{2
class DriverView(View):
    """Render drivers page"""

    def get(self, request):
        dl = Driver.objects.all()
        ctx = {"driver_list": dl}
        return render(request, "erp_app/driver_list.html", ctx)


class DriverCreate(View):
    template = "erp_app/driver_form.html"
    success_url = reverse_lazy("erp_app:driver_list")

    # Create a form to add a driver
    def get(self, request):
        form = DriverForm()
        ctx = {"form": form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = DriverForm(request.POST)
        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template, ctx)
        driver = form.save()
        return redirect(self.success_url)


class DriverUpdate(View):
    model = Driver
    success_url = reverse_lazy("erp_app:driver_list")
    template = "erp_app/driver_form.html"

    # Pull the form by primary key (pk)
    def get(self, request, pk):
        driver = get_object_or_404(self.model, pk=pk)
        form = DriverForm(instance=driver)
        ctx = {"form": form}
        return render(request, self.template, ctx)

    # Save changes
    def post(self, request, pk):
        driver = get_object_or_404(self.model, pk=pk)
        form = DriverForm(request.POST, instance=driver)
        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class DriverDelete(View):
    model = Driver
    success_url = reverse_lazy("erp_app:driver_list")
    template = "erp_app/driver_confirm_delete.html"

    def get(self, request, pk):
        driver = get_object_or_404(self.model, pk=pk)
        form = DriverForm(instance=driver)
        ctx = {"driver": driver}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        driver = get_object_or_404(self.model, pk=pk)
        driver.delete()
        return redirect(self.success_url)


# }}} 2


# TruckView {{{3
class TruckView(View):
    def get(self, request):
        tl = Truck.objects.all()
        ctx = {"truck_list": tl}
        return render(request, "erp_app/truck_list.html", ctx)


class TruckCreate(View):
    template = "erp_app/truck_form.html"
    success_url = reverse_lazy("erp_app:truck_list")

    # Create a form to add a driver
    def get(self, request):
        form = TruckForm()
        ctx = {"form": form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = TruckForm(request.POST)
        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template, ctx)
        truck = form.save()
        return redirect(self.success_url)


class TruckUpdate(View):
    model = Truck
    success_url = reverse_lazy("erp_app:truck_list")
    template = "erp_app/truck_form.html"

    # Pull the form by primary key (pk)
    def get(self, request, pk):
        truck = get_object_or_404(self.model, pk=pk)
        form = TruckForm(instance=truck)
        ctx = {"form": form}
        return render(request, self.template, ctx)

    # Save changes
    def post(self, request, pk):
        truck = get_object_or_404(self.model, pk=pk)
        form = TruckForm(request.POST, instance=truck)
        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class TruckDelete(View):
    model = Truck
    success_url = reverse_lazy("erp_app:truck_list")
    template = "erp_app/truck_confirm_delete.html"

    def get(self, request, pk):
        truck = get_object_or_404(self.model, pk=pk)
        form = TruckForm(instance=truck)
        ctx = {"truck": truck}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        truck = get_object_or_404(self.model, pk=pk)
        truck.delete()
        return redirect(self.success_url)


# }}}3


# TrailerView {{{4
class TrailerView(View):
    def get(self, request):
        trl = Trailer.objects.all()
        ctx = {"trailer_list": trl}
        return render(request, "erp_app/trailer_list.html", ctx)


class TrailerCreate(CreateView):
    model = Trailer
    fields = "__all__"
    success_url = reverse_lazy("erp_app:trailer_list")


class TrailerUpdate(UpdateView):
    model = Trailer
    fields = "__all__"
    success_url = reverse_lazy("erp_app:trailer_list")


class TrailerDelete(DeleteView):
    model = Trailer
    fields = "__all__"
    success_url = reverse_lazy("erp_app:trailer_list")


# }}}4


# LoadView {{{5
class LoadView(View):
    def get(self, request):
        ld = Load.objects.all()
        ctx = {"load_list": ld}
        return render(request, "erp_app/load_list.html", ctx)


class LoadCreate(CreateView):
    model = Load
    form_class = LoadForm
    success_url = reverse_lazy("erp_app:load_list")

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs["driver_id"] = self.request.GET.get("driver")
        return kwargs


class LoadUpdate(UpdateView):
    model = Load
    fields = "__all__"
    success_url = reverse_lazy("erp_app:load_list")


class LoadDelete(DeleteView):
    model = Load
    fields = "__all__"
    success_url = reverse_lazy("erp_app:load_list")


# }}}5


# PayrollView {{{6
class PayrollView(View):
    def get(self, request):
        pr = Payroll.objects.all()
        ctx = {"payroll_list": pr}
        return render(request, "erp_app/payroll_list.html", ctx)


class PayrollCreate(CreateView):
    model = Payroll
    form_class = PayrollForm
    success_url = reverse_lazy("erp_app:payroll_list")

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.success_url)


class PayrollUpdate(UpdateView):
    model = Payroll
    form_class = PayrollForm
    success_url = reverse_lazy("erp_app:payroll_list")

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.success_url)


class PayrollDelete(DeleteView):
    model = Payroll
    fields = "__all__"
    success_url = reverse_lazy("erp_app:payroll_list")


# }}}6


def contact_list(request):
    return render(request, "erp_app/contact_list.html")
