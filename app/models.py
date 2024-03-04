from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    Product_category_id=models.IntegerField(primary_key=True)
    Product_category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.Product_category_name
    
class Product(models.Model):
    Product_category_id=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    Product_id=models.IntegerField()
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField()
    product_brand=models.CharField(max_length=50)

    def __str__(self):
        return self.product_name
    