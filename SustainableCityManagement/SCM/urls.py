from django.urls import path
from SCM.views import (
    login_view,
    ValidateLoginView,
    DisplayMapView
    )

app_name = "SCM"
urlpatterns = [
    path('home/', ValidateLoginView, name='validate-login'),
    path('traffic/', DisplayMapView, name='display-map')
]