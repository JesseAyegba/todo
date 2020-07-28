from django.contrib import admin
from django.urls import path, include
from user_reg import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/",user_views.login_page, name="login"),
    path("logout/", user_views.logout_page, name="logout"),
    path("user_reg/", user_views.user_registration, name="user_registration"),
    path("", include("todo_app.urls")),
]