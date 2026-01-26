from django.db import models
from django.contrib.contenttypes.models import ContentType # to use as a generic class
from django.contrib.contenttypes.fields import GenericForeignKey # to use for filling in the tagged object's type
# here we will define 2 classes for the tag app:
# one tag can be applied to multiple items --> Tag and TaggedItem has a 1-* relationship



class Tag(models.Model):
    label = models.CharField(max_length= 255)

class TaggedItem(models.Model): # what tag is applied to what object?
    tag = models.ForeignKey(Tag, on_delete= models.CASCADE) # once you delete a tag, unmark the items (i.e. remove them from this db)
    # now, to keep this app reusable (for tagging other objects), we need to write some code of 'generic' nature
    # to find any instance in any data table, we need the type (class name?), and the ID (to find the record)
    # use contenttypes app
    content_type = models.ForeignKey(ContentType, on_delete= models.CASCADE) # once you delete a table, then untag every item that is a record in that table
    object_id = models.PositiveIntegerField() # assumed to be a primary key
    # now in order to read the actual name of the object that is tagged, we do the following
    object_type = GenericForeignKey()



