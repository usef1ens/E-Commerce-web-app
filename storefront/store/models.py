from django.db import models
# models tells your database how to organize the data in python form
# every field defines a column in the database
# avoids writing sql


class Customer(models.Model):
    MEMBERSHIP_CHOICES = [ ('G','Gold'),
                           ('S','Silver'),
                           ('B','Bronze') ]
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length = 40, unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null= True)
    membership = models.CharField(max_length = 1, choices=MEMBERSHIP_CHOICES, default= 'B')



#NOTE:DJANGO automatically generates IDs for every instance for an entity
# NOTE: IF you want to create primary keys, just choose the primary key option for a variable, 
# and django will not generate IDs for the instances of the corresponding class

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Complete'),
        ('F', 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add = True)
    payment_status = models.CharField(max_length = 1, choices= PAYMENT_CHOICES, default= 'P')
    customer = models.ForeignKey(Customer, on_delete= models.PROTECT)

# every customer has one address, and every address belongs to one customer -> 1-1 relationship
# customer is the parent in this relationship, and address is the child
class Adress(models.Model):
    street = models.CharField(max_length= 255)
    city = models.CharField(max_length= 255)
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE, primary_key= True)
    # when the customer is deleted, the address is also deleted, and the customer is linked by the 
    # above data field

class Collection(models.Model):
    title = models.CharField(max_length= 255)

class Cart(models.Model):
    title = "" # tentative

# let us define a class for products and make it inherit the Model class from models
class Product(models.Model):
    title = models.CharField(max_length=255) # mandatory parameter for defining max length
    description = models.TextField() # has no upper limit
    price = models.DecimalField(max_digits=6, decimal_places=2) # FloatField has rounding issues
    # so use DecimalField for prices
    # here we allow the max price to be max 9999.99
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey(Collection, on_delete = models.PROTECT)
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
# NOTE: an instance of this class is a ROW in the database
'''
NOTE:
In this model, I define the following relationships:
Customer and Adress is 1-1
collection and products is 1-*
customer and orders is 1-*
order and items is 1-*
cart and items is 1-*
'''



