from django.urls import path
from . import views


urlpatterns = [
    path("", views.landing, name="landing"),
    path("dashboard/", views.home, name="home"),
    path("delete/<str:item_id>/", views.delete_item, name="delete-item"),
    path("update/<str:item_id>/", views.update_item, name="update"),
    path("clear_list/", views.clear_list, name="clear_list"),
]