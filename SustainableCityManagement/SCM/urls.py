from django.urls import path
from SCM.views import (
    login_view,
    validate_login_view
    )

app_name = "SCM"
urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', validate_login_view, name='validate_login')
]