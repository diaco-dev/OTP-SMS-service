import requests
import json

def send_sms(receptor, variables, pattern_code):
    url = f"https://api.kavenegar.com/v1/{setting.KAVENEGAR_API_KEY}/verify/lookup.json"
    payload = {
        'receptor': receptor,
        'template': pattern_code,
        'token': variables.get('verification-code'),  # Match the key from variables
        'type': 'sms'
    }
    logger.info(f"Sending SMS to {receptor} with payload: {payload}")
    try:
        response = requests.post(url, data=payload, timeout=10)  # Add timeout
        logger.info(f"Response status: {response.status_code}")
        logger.info(f"Response text: {response.text}")
        if response.status_code == 200:
            result = response.json()
            if result.get('return', {}).get('status') == 200:
                logger.info(f"SMS sent successfully to {receptor}")
            else:
                logger.error(f"API error: {result}")
        else:
            logger.error(f"Error sending SMS: {response.status_code} - {response.text}")
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error in send_sms: {e}", exc_info=True)
        return None