from rest_framework import serializers
from . models import Product

class ProductSerializer(serializers.ModelSerializer):
    # product_name = serializers.CharField(source='Product.product_name')
    class Meta:
        model=Product
        # fields='__all__'
        # fields=['id','product_user','product_name','product_description','product_price']
        fields=['product_user','product_name','product_description','product_price']
        

