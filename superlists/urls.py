from django.contrib import admin
from django.urls import path
from lists import views

urlpatterns = [
    path("", views.home_page, name="home"), 
    path('admin/', admin.site.urls),
    path("lists/the-only-list-in-the-world/", views.view_list, name="view_list"), 
]
