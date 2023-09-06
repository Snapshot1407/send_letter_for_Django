from django.urls import path
# Импортируем созданные нами представления
from .views import AppointmentView

urlpatterns = [path(r'',AppointmentView.as_view()), ]