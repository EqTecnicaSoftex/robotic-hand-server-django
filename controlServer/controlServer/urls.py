from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('control-denso/', views.send_control_denso, name='send_control'),
    path('control-hand/', views.send_control_hand, name='send_control'),
    path('move-denso/', views.move_denso, name='move_denso'),
    path('captured-object/', views.captured, name='finalize_denso'),
    path('released-object/', views.released, name='released_object'),
    path('server-status/', views.server_status, name='server_status')
]
