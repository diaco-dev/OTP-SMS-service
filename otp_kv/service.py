

# ---------------------------------------------------------------------------------------------------------------------
# send code mobile save code in db
# ---------------------------------------------------------------------------------------------------------------------
class SendCodeSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=100)

    def validate(self, data):
        mobile = data.get('mobile')

        if not (mobile.isdigit() and len(mobile) == 11):
            raise serializers.ValidationError("The mobile number format is incorrect")

        if User.objects.filter(mobile=mobile).exists():
            raise serializers.ValidationError("Mobile number is already registered.")

        # genarate code on redis
        verification_code = ''.join(random.choices(string.digits, k=6))

        # save in redis for 120s
        redis_conn = get_redis_connection("default")
        redis_conn.setex(f"verification_code:{mobile}", 120, verification_code)

        # send code on redis
        send_verification_sms.delay(mobile, verification_code)

        return data
# ---------------------------------------------------------------------------------------------------------------------
# send code mobile
# ---------------------------------------------------------------------------------------------------------------------
class SendCodeView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = SendCodeSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "send code."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
