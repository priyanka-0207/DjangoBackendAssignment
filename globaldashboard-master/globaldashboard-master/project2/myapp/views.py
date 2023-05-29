from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import CustomUser
from myapp.utils import generateOTP
from django.shortcuts import render

def login_page(request):
    return render(request, 'myapp/login.html')

def signup_page(request):
    return render(request, 'myapp/signup.html')

def logout_page(request):
    return render(request, 'myapp/logout.html')

def search_page(request):
    return render(request, 'myapp/search.html')

class SignupView(APIView):
    def post(self, request):
        try:
            print(request.data)
            data = {}
            for element in request.data:
                data[element['name']]=element['value']
            
            if CustomUser.objects.filter(email=data['email']):
                raise ValueError("User already exists!")
            user = CustomUser(email=data['email'],first_name=data['fname'],last_name=data['lname'],gender=data['gender'],phone_number=data['pnumber'])
            user.save()
            return Response({'Success': 'Welcome to myapp', 'data':data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        try:
            print(request.data)
            pnumber = request.data.get('pnumber')
            otp = request.data.get('otp')
            users = CustomUser.objects.filter(phone_number=pnumber)
            for user in users:
                if user.otp == otp:
                    return Response({'Success': 'Welcome to myapp'}, status=status.HTTP_200_OK)            
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class SendOtpView(APIView):
    def post(self,request):
        print(request.data)
        pnumber = request.data.get("pnumber")
        users = CustomUser.objects.filter(phone_number=pnumber)
        if not users:
            return Response({'error':'User not yet registered'},status=status.HTTP_404_NOT_FOUND)
        
        otp = generateOTP(pnumber)
        for user in users:
            user.otp = otp
            user.save()
        
        return Response({'Success':'OTP Sent'}, status=status.HTTP_200_OK)