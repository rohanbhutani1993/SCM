from django.urls import path
from SCM.views import (
    login_view,
    ValidateLoginView,
    DisplayMapView,
    DisplayPollutionData,
    DisplayDublinBusData,
    DisplayEventsData,
    DisplayDublinBikesData,
    push_notify
    )

app_name = "SCM"
urlpatterns = [
    path('Home/', ValidateLoginView, name='validate-login'),
    path('Traffic/', DisplayMapView, name='traffic-data'),
    path('PollutionData/', DisplayPollutionData, name='pollution-data'),
    path('DublinBus/', DisplayDublinBusData, name='bus-data'),
    path('Events/', DisplayEventsData, name='event-data'),
    path('DublinBikes/',DisplayDublinBikesData, name='bikes-data'),
    path('PushNotification/', push_notify, name='push-notification')


]