# OTP-SMS-service
you can send SMS code and verify user phone number

# OTP SMS Project

This is a Django Rest Framework (DRF) application that provides functionality for sending and verifying One-Time Passwords (OTPs) via SMS. The project is structured with a main configuration folder (`config`) and an application named `otp_fz` for FARAZSMS service and `otp_kv` for KAVEHNEGAR.

## Project Structure
- **`config/`**: Contains the main Django settings and configuration files (e.g., `settings.py`, `urls.py`, etc.).
- **`otp/`**: The Django app responsible for OTP generation, SMS integration, and verification logic.
- **`requirements.txt`**: Lists all Python dependencies required to run the project.

## Features
- Generate and send OTPs via SMS.
- Verify OTPs submitted by users.
- RESTful API endpoints built with Django Rest Framework.

## Prerequisites
- Python 3.x
- Django
- Django Rest Framework
- An SMS gateway service - configure API keys in settings.
- IPPANEL_API_KEY
- KAVENEGAR_API_KEY 

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shilahsa/OTP-SMS-service.git
   cd OTP-SMS-service
   
