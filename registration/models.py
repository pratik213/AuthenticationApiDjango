
from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Base Manager is here
class CustomAccountManager(BaseUserManager):
    def create_superuser(self,email,user_name,password,**other_fields):
        
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(gettext_lazy("Super user must be assigned to is_staff = True"))

        if other_fields.get('is_superuser') is not True:
            raise ValueError(gettext_lazy("Super user must be assigned to is_super = True"))
        

        return self.create_user(email=email,user_name=user_name,password=password,**other_fields)




    def create_user(self,email,user_name,*args,password,**kwargs):
        
        if not email:
            raise ValueError(gettext_lazy("You must enter email id"))

        if 'user_name' in kwargs:
            user_name=kwargs['user_name']

        elif 'company_name' in kwargs:
            user_name=kwargs['company_name']


        email=self.normalize_email(email)
        user_name=user_name or company_name
        user=self.model(email=email,user_name=user_name,**kwargs)
        user.set_password(password)
        user.save()
        return user


# Create your models here.
class RegisterUser(AbstractBaseUser,PermissionsMixin):
    User_Choices=[
    ('customer','customer'),
    ('seller','seller'),

]
    
    company_name=models.CharField(max_length=150)
    email=models.EmailField(gettext_lazy('email address'),unique=True)
    user_name=models.CharField(max_length=150,unique=True)
    address=models.CharField(max_length=150)
    phone_number = models.CharField(max_length=12,blank=True,null=True,unique=True)
    user_type=models.CharField(choices=User_Choices,max_length=50)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    objects=CustomAccountManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['user_name' or 'company_name']

    def __str__(self):
        return self.user_name or self.company_name

class UserProfile(models.Model):
    user=models.OneToOneField(RegisterUser, on_delete=models.CASCADE)
    bio=models.TextField(max_length=500)

    def __str__(self):
        return self.user.user_name