from django.db import models


#product_id(int); product_name(String); date(String: "dd-mm-yyyy"); inventory_level(int)


class Product(models.Model):
    product_name = models.CharField(max_length=250, null=False, default='')
    date = models.DateField(null=False, auto_now_add=True)
    inventory_level = models.IntegerField(null=False)
