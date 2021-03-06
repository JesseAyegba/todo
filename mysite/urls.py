from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from user_reg import views as user_views


urlpatterns = [
    path("my_administration/", admin.site.urls),
    path("login/",user_views.login_page, name="login"),
    path("logout/", user_views.logout_page, name="logout"),
    path("user_reg/", user_views.user_registration, name="user_registration"),
    path("", include("todo_app.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

