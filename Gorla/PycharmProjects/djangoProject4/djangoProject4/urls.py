from django.contrib import admin
from django.urls import path
from DpApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view),
]