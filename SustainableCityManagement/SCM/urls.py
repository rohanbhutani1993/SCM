from django.urls import path
from SCM.views import (
    login_view,
    ValidateLoginView,
    DisplayMapView,
    DisplayPollutionData
    )

app_name = "SCM"
urlpatterns = [
    path('home/', ValidateLoginView, name='validate-login'),
    path('traffic/', DisplayMapView, name='display-map'),
    path('pollution', DisplayPollutionData, name='display-pollution')
]