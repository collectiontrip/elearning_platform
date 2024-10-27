import random
from django.core.mail import send_mail
from django.conf import settings


def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    
    subject = "Your OTP Code"
    message = f"Use this OTP to log in: {otp}, It will expire in 5 minutes."
    
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
    
