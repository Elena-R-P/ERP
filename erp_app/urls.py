from django.urls import include, path
from . import views

app_name = "erp_app"


urlpatterns = [
    path("", views.index, name="index"),
    path("drivers/", views.drivers_list, name="drivers_list"),
    path("trucks/", views.trucks_list, name="trucks_list"),
    path("trailers", views.trailers_list, name="trailers_list"),
    path("loads/", views.loads_list, name="loads_list"),
    path("payroll/", views.payroll, name="payroll"),
    path("contacts/", views.contacts_list, name="contacts_list"),
    path("driver_add/", views.driver_add, name="driver_add"),
]
