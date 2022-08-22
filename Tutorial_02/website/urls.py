from django.contrib import admin
from django.urls import path
 
from hello_world import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="homepage") 
]