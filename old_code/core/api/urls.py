from django.urls import path, include
from .views import DoctorsAPIView, DoctorIdAPIView


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('Accounts/', include('account.urls')),
    path('Authentication/', include('authentication.urls')),
    path("Hospitals/", include('hospital.urls')),
    path("Timetable/", include('time_table.urls')),
    path("Doctors/", DoctorsAPIView.as_view()),
    path("Doctors/<int:id>/", DoctorIdAPIView.as_view())
]