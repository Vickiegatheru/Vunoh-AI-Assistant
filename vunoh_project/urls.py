from django.contrib import admin
from django.urls import path
from assistant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('process/', views.process_request, name='process_request'),
    path('update/<int:task_id>/', views.update_status, name='update_status'),
]