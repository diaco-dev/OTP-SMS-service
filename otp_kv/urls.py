from django.urls import path, include
from rest_framework.routers import DefaultRouter
from otp_kv.service import SendCodeView

router = DefaultRouter()
app_name = 'otp_fz'

urlpatterns = [
    path('', include(router.urls)),
    #---------------- send AnonymousMobile ----------------------#
    path('send-code/', SendCodeView.as_view(), name='send_code'),

]