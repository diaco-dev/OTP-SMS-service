from datetime import timezone, timedelta
from random import randrange
from django.conf import settings
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from user.models import User
from user.serializer import AnonymousMobileVerificationSerializer,LoginSerializer
from otp_fz.tasks import send_verification_sms
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken

# ---------------------------------------------------------------------------------------------------------------------
# log-in with email/mobile
# ---------------------------------------------------------------------------------------------------------------------
class CustomLoginView(APIView):
    permission_classes = (AllowAny,)
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=status.HTTP_200_OK)