

class AnonymousMobileVerificationSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(max_length=11, min_length=11, required=True)

    class Meta:
        model = User
        fields = ('mobile',)

    def validate_mobile(self, value):
        if not value.isdigit():
            raise serializers.ValidationError({"mobile": 'Mobile number can only be numerical'})
        if value[:2] != '09':
            raise serializers.ValidationError({"mobile": 'mobile no must start with "09"'})
        return value

# ---------------------------------------------------------------------------------------------------------------------
# SEND CODE Mobile      SMS
# ---------------------------------------------------------------------------------------------------------------------
class VerifyMobileNumber(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AnonymousMobileVerificationSerializer # send to AnonymousMobile

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            mobile = serializer.validated_data['mobile']
            user = User.objects.filter(mobile=mobile).first()

            if not user:
                return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

            user.verify_mobile_generic_code = str(randrange(100000, 999999))
            user.verify_mobile_generic_code_expire_at = timezone.now() + timedelta(
                seconds=settings.MOBILE_VERIFICATION_EXPIRE + 10)
            user.save()

            send_verification_sms({
                'mobile': mobile,
                'code': user.verify_mobile_generic_code
            })
            return Response({
                #  ToDo:  WARNING: remove this line
                'code': user.verify_mobile_generic_code,
                'timeout': settings.MOBILE_VERIFICATION_EXPIRE
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)