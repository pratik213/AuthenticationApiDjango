from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from . serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.
class Product(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request,format=None):
        user=self.request.user
        product=user.p_user.get()
        serializer=ProductSerializer(product)
        # import pdb;pdb.set_trace()
        return Response(serializer.data)
    
    def put(self,request,format=None):
        user=request.user
        
        data=request.data.copy()
        
        data["user"]=user
            
        serializer=ProductSerializer(request.user.p_user.get(),data=data,partial=True)
        
        header=request.headers
        # import pdb;pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            # import pdb;pdb.set_trace()
            return Response(serializer.data)
        return Response(serializer.errors)

    def post(self,request,format=None):
        user=request.user
        data=request.data.copy()
        #my product_user currently logged in value will be automatically assigned to the data
        data["product_user"]=user.pk
        serializer=ProductSerializer(request.user.p_user.first(),data=data)
        
        if serializer.is_valid():
            # import pdb;pdb.set_trace()
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    
