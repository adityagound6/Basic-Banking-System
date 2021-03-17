from django.contrib import admin
from django.urls import path
from .views import home,viewcustomer,transection,transection_history
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home,name='home'),
    path('viewcustomer',viewcustomer,name='viewcustomer'),
    path('transection/<str:slug>',transection,name='transection'),
    path('transection_history',transection_history,name='transection_history'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
