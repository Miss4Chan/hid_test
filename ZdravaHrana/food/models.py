from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#Креирајте Djangо апликација за менаџирање на продавница за здрава храна. 

# За секој клиент се чува име, презиме, адреса и емаил. MODEL
class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
#За секоја категорија се чува име, опис и дали е активна (bool). MODEL
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Categories"

#Секој прехранбен продукт се карактеризира со автоматски генерирана шифра, MODEL
#име, опис и информација за тоа во која категорија припаѓа, корисникот кој го креирал продуктот, 
#фотографија од продуктот, цена и количина. 
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(Client,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="tuka/", null=True)
    price = models.FloatField()
    quantity = models.IntegerField()

#За секоја продажба во системот се евидентираат продуктите кои биле продадени (секој со соодветна количина),
#атумот на продажба и клиентот кој ги купил.  MODEL
class Sale(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    date = models.DateField()

class ProductsInSale(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    sale  = models.ForeignKey(Sale, on_delete=models.CASCADE)
    amount = models.IntegerField()



