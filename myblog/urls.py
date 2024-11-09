from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detail",views.detail,name="detail"),
    path("about",views.about,name="about"),
    path("new_url",views.new_url_view,name ="new_url"),
    path("old_url",views.old_url_redirect,name ="old_url"),
    path('admin/', admin.site.urls),
]
