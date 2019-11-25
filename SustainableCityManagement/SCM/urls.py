from django.urls import path
from SCM.views import (
    login_view,
    ValidateLoginView,
    DisplayMapView,
    DisplayPollutionData,
    DisplayDublinBusData,
    DisplayEventsData,
    push_notify
    )

app_name = "SCM"
urlpatterns = [
    path('home/', ValidateLoginView, name='validate-login'),
    path('traffic/', DisplayMapView, name='traffic-data'),
    path('pollution/', DisplayPollutionData, name='pollution-data'),
    path('DublinBus/', DisplayDublinBusData, name='bus-data'),
    path('events/', DisplayEventsData, name='event-data'),
    path('PushNotificaiotn', push_notify, name='push-notification')



]