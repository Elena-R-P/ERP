from django.urls import include, path
from . import views

app_name = "erp_app"


urlpatterns = [
    path("", views.index, name="index"),
    path("drivers/", views.DriverView.as_view(), name="driver_list"),
    path("drivers/create/", views.DriverCreate.as_view(), name="driver_create"),
    path(
        "drivers/<int:pk>/update/", views.DriverUpdate.as_view(), name="driver_update"
    ),
    path(
        "drivers/<int:pk>/delete/", views.DriverDelete.as_view(), name="driver_delete"
    ),
    path("trucks/", views.TruckView.as_view(), name="truck_list"),
    path("trucks/create/", views.TruckCreate.as_view(), name="truck_create"),
    path("trucks/<int:pk>/update/", views.TruckUpdate.as_view(), name="truck_update"),
    path("trucks/<int:pk>/delete/", views.TruckDelete.as_view(), name="truck_delete"),
    path("trailers/", views.TrailerView.as_view(), name="trailer_list"),
    path("trailers/create/", views.TrailerCreate.as_view(), name="trailer_create"),
    path(
        "trailers/<int:pk>/update/",
        views.TrailerUpdate.as_view(),
        name="trailer_update",
    ),
    path(
        "trailers/<int:pk>/delete/",
        views.TrailerDelete.as_view(),
        name="trailer_delete",
    ),
    path("loads/", views.LoadView.as_view(), name="load_list"),
    path("loads/create/", views.LoadCreate.as_view(), name="load_create"),
    path("loads/<int:pk>/update/", views.LoadUpdate.as_view(), name="load_update"),
    path("loads/<int:pk>/delete/", views.LoadDelete.as_view(), name="load_delete"),
    path("payroll/", views.payroll_list, name="payroll_list"),
    path("contacts/", views.contact_list, name="contact_list"),
]
