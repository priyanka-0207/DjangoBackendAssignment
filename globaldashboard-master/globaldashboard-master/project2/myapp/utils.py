from django.core.mail import EmailMessage
from django.conf import settings
from myapp.models import CustomUser
from twilio.rest import Client
import random

client = Client("AC1bbf78a8cad1854e0b9f8b33fb642291", "b9fd881818cace88527010aa815ea612")

def send_otp(email):
    # Generate the OTP
    otp = random.randint(100000, 999999)

    # Compose the email message
    subject = 'OTP Verification'
    message = f'Your OTP is: {otp}'
    from_email = settings.EMAIL_HOST_USER
    to_email = email

    # Send the email
    email = EmailMessage(subject, message, from_email, [to_email])
    email.send()

    # Return the OTP
    return otp

def generateOTP(phone_number):
    otp = random.randint(100000, 999999)
    # message = client.messages.create(body=f"Your OTP is: {otp}",from_="+13156311922",to=phone_number)
    return otp