from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('control-denso/', views.send_control_denso, name='send_control'),
    path('control-hand/', views.send_control_hand, name='send_control'),
    path('move-denso/', views.move_denso, name='move_denso'),
    path('finalize-denso/', views.finalize_denso, name='finalize_denso'),
]
