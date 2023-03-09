from rest_framework import serializers
from . models import RegisterUser,UserProfile
from django.db.models import Q

class CustomerSerializer(serializers.ModelSerializer):
    #to use confirm password field
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=RegisterUser
        fields=['email','user_name','phone_number','password','password2','user_type']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self,validate_data):
        return RegisterUser.objects.create_user(**validate_data)


class SellerSerializer(serializers.ModelSerializer):
    #to use confirm password field
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=RegisterUser
        fields=['email','user_name','company_name','phone_number','password','password2','user_type']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self,validate_data):
        return RegisterUser.objects.create_user(**validate_data)





class CustomerLoginSerializer(serializers.ModelSerializer):
    email_or_phone_number=serializers.CharField(max_length=255,required=True)
    password = serializers.CharField(max_length=128, write_only=True)
    class Meta:
        model=RegisterUser
        fields=['email_or_phone_number','password']

    def validate(self,attrs):
        email_or_phone_number=attrs.get('email_or_phone_number')
        password=attrs.get('password')

        user=RegisterUser.objects.filter(
            Q(email=email_or_phone_number) | Q(phone_number=email_or_phone_number)
        ).first()

        if not user:
            raise serializers.ValidationError("User not found with given email/password")

        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect Password")

        attrs['user']=user
        return attrs
        
class SellerLoginSerializer(serializers.ModelSerializer):
    email_or_phone_number=serializers.CharField(max_length=255,required=True)
    password = serializers.CharField(max_length=128, write_only=True)
    # import pdb;pdb.set_trace()
    class Meta:
        model=RegisterUser
        fields=['email_or_phone_number','password']

    def validate(self,attrs):
        email_or_phone_number=attrs.get('email_or_phone_number')
        password=attrs.get('password')

        user=RegisterUser.objects.filter(
            Q(email=email_or_phone_number) | Q(phone_number=email_or_phone_number)
        ).first()

        if not user:
            raise serializers.ValidationError("User not found with given email/password")

        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect Password")

        attrs['user']=user
        return attrs

  

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        # fields=['id','user','bio']
        fields=['id','bio']
        # depth=1