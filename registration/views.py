from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from . models import RegisterUser
from .serializers import CustomerSerializer,SellerLoginSerializer,CustomerLoginSerializer,UserProfileSerializer,SellerSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken



#Generating token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class CustomerRegisterView(APIView):
    def post(self,request,format=None):
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'Registration Sucess'})
        return Response(serializer.errors)

class SellerRegisterView(APIView):
    def post(self,request,format=None):
        serializer=SellerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'Registration Sucess'})
        return Response(serializer.errors)


class CustomerLoginView(APIView):
    def post(self,request,format=None):
        serializer=CustomerLoginSerializer(data=request.data)
        
        
        
        if serializer.is_valid(raise_exception=True):
            # import pdb;pdb.set_trace()
            email=serializer.data.get('email_or_phone_number')
            password=serializer.validated_data.get('password')
            
            user=authenticate(email=email,password=password)
            # import pdb;pdb.set_trace()
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,'msg':'login sucess'})
            else:
                return Response({'errors':{'non_field_errors':['Email or password is not valid']}})
        return Response(serializer.errors)

class SellerLoginView(APIView):
    # import pdb;pdb.set_trace()
    def post(self,request,format=None):
        serializer=SellerLoginSerializer(data=request.data)
        # import pdb;pdb.set_trace()
        
        
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email_or_phone_number')
            password=serializer.validated_data.get('password')
            email=validate_email_or_phone_number(email)
            
            # import pdb;pdb.set_trace()
            user=authenticate(email=email,password=password)
            # import pdb;pdb.set_trace()
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,'msg':'login sucess'})
            else:
                return Response({'errors':{'non_field_errors':['Email or password is not valid']}})
        return Response(serializer.errors)





class UserProfileView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request,format=None):
        serializer=UserProfileSerializer(request.user)
        # import pdb;pdb.set_trace()
        return Response(serializer.data)
    
    def put(self,request,format=None):
        user=request.user
        data=request.data.copy()
        data["user"]=user
            
        serializer=UserProfileSerializer(request.user,data=data,partial=True)
        header=request.headers
        # import pdb;pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            # import pdb;pdb.set_trace()
            return Response(serializer.dataaaaa)
        return Response(serializer.errors)
    









#thid function is used so that if the user enters phone number ,the associated email of that phone number will be taken
# and if user enters email than the email will be taken for authentication


import re

def validate_email_or_phone_number(data):
    if re.match(r'^\+?[0-9]{10,12}$', data):
        # if data matches phone number pattern
        # extract email from phone number
        user = RegisterUser.objects.filter(phone_number=data).first()
        if user:
            return user.email
    elif re.match(r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$', data):
        # if data matches email pattern
        return data
    else:
        raise serializers.ValidationError('Enter a valid email or phone number')






# @api_view(['POST'])
# def register_customer(request):
#     #Used for debugg
#     # import pdb;pdb.set_trace()
#     serializer=CustomerSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=200)
#     return Response(serializer.errors,status=400)


# @api_view(['POST'])
# def register_seller(request):
#     serializer=SellerSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=200)
#     return Response(serializer.errors,status=400)


