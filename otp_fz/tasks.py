from celery import shared_task
from otp_fz.sms import send_sms

@shared_task
def send_verification_sms(params):
    mobile = params['mobile']
    code = params['code']
    variables = {
        "verification-code": code
    }
    send_sms(mobile, variables, 'x7a68g929i09924')
