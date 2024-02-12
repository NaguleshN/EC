from django.db import models

# Create your models here.
status=(('Active','Active'),('Inactive','Inactive'),)
class SolarPanel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    model_number = models.CharField(max_length=20)
    nominal_voltage = models.PositiveIntegerField()
    product_weight =  models.PositiveIntegerField()
    dimensions_l =models.PositiveIntegerField()
    dimensions_b =models.PositiveIntegerField()
    dimensions_w =models.PositiveIntegerField()
    warranty = models.PositiveIntegerField()
    status=models.CharField(choices=status,max_length=10,default='Inactive')
    
    def __str__(self):
        return self.name
    
class Maintainance(models.Model):
    product = models.ForeignKey(SolarPanel,on_delete=models.CASCADE)
    maintainance_details = models.CharField(max_length=500)
    price= models.IntegerField()
    def __str__(self):
        return self.product.name 