from celery import shared_task
from otp_kv.sms import send_sms
import requests
from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def send_verification_sms(mobile, code):
    logger.info(f"Starting to send SMS to {mobile} with code {code}")
    try:
        variables = {
            "verification-code": str(code)
        }
        response = send_sms(mobile, variables, 'ibc-otp')
        if response and response.status_code == 200:
            logger.info(f"Verification SMS sent to {mobile}")
        else:
            raise Exception("Failed to send SMS")
    except Exception as e:
        logger.error(f"Error in send_verification_sms: {e}", exc_info=True)
        raise  # For Celery retry