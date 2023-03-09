from django.db import models
from registration.models import RegisterUser

class Product(models.Model):
    product_user=models.ForeignKey(RegisterUser, on_delete=models.PROTECT,related_name="p_user")
    # import pdb;pdb.set_trace()
    product_name=models.CharField(max_length=255)
    product_description=models.CharField(max_length=755)
    product_price=models.IntegerField()




