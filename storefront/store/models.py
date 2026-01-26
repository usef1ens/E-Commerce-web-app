from django.db import models
# models tells your database how to organize the data in python form
# every field defines a column in the database
# avoids writing sql

'''
NOTE:
In this model, I define the following relationships:
Customer and Adress is 1-1
collection and products is 1-*
products and collection is 1-* --> this and the relationship in the previous line are not a *-* relationship!
customer and orders is 1-*
order and items is 1-*
cart and items is 1-*
promotions and products is *-*
'''

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
    '''
    The on_delete behavior is PROTECT, since we do not want to delete an order from our database, since they represent sales.
    to prevent orphaned data (orders without associated profiles), one must first delete the orders before deleting the customer profile
    '''

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
    featured_product = models.ForeignKey('Product', on_delete= models.SET_NULL, null= True, related_name= '+')  # since I do not want to delete the collection, even if a featured product has been deleted from it
    # apparantly, we do not want to define the reverse relationship here, so the product can not see the collections it is in
    # only collections can see what product they have
class Cart(models.Model):
    title = models.CharField(max_length= 255)

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
    promotions = models.ManyToManyField('Promotion', related_name = 'products') # modelling *-* relations, using the related name, django will rename the reverse relationship in the promotion class as 'products'
    ''' 
    we used PROTECT for the delete behavior, 
    so that if we can not delete a collection, before reassigning the products, or deleting the products manually.
    This also prevents us from deleting the individual products, if we would delete a collection
    '''

    #cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
# NOTE: an instance of this class is a ROW in the database



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete= models.PROTECT) # do not delete an order, before deleting the ordered Items
    product = models.ForeignKey(Product, on_delete= models.PROTECT) # do not delete a product in stock, before deleting the orders of that product
    quantity = models.PositiveSmallIntegerField() # to prevent negative values
    unit_price = models.DecimalField(max_digits= 6, decimal_places= 2) # to record CURRENT price of the ordered item

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add= True) # to auto-populate the column with the current time it was created

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE) # if I delete a cart, then discard all cart items
    product = models.ForeignKey(Product, on_delete= models.CASCADE) # if I delete a product, then the cart item corresponding to it must be also discarded
    quantity = models.PositiveSmallIntegerField()

class Promotion(models.Model):
    description = models.CharField(max_length= 255)
    discount = models.DecimalField(max_digits= 5, decimal_places= 2) # needs a validator in order not to input numbers above 100%


