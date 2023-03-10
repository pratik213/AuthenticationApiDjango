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
        product=user.p_user.all()
        serializer=ProductSerializer(product,many=True)
        # import pdb;pdb.set_trace()
        return Response(serializer.data)
    
    def put(self,request,id,format=None):
        user=request.user
        
        data=request.data.copy()
        
        data["user"]=user
        # import pdb;pdb.set_trace()
            
        serializer=ProductSerializer(request.user.p_user.get(id=id),data=data,partial=True)
        # import pdb;pdb.set_trace()
        
        # header=request.headers
        # import pdb;pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            # import pdb;pdb.set_trace()
            return Response(serializer.data)
        return Response(serializer.errors)

    def post(self,request,format=None):
        user=request.user
        data=request.data.copy()
        # data=request.data
        # import pdb;pdb.set_trace()
        #my product_user currently logged in value will be automatically assigned to the data
        data["product_user"]=user.pk
        serializer=ProductSerializer(data=data)
        # import pdb;pdb.set_trace()

        
        if serializer.is_valid():
            # import pdb;pdb.set_trace()
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    
