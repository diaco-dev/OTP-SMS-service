from django.urls import path, include
from rest_framework.routers import DefaultRouter
from otp_fz.service import VerifyMobileNumber
router = DefaultRouter()
app_name = 'otp_fz'

urlpatterns = [
    path('', include(router.urls)),
    #---------------- send AnonymousMobile ----------------------#
    path('send-code/', VerifyMobileNumber.as_view(), name='send_code'),

]