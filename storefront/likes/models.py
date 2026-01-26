from django.db import models
from django.contrib.auth.models import User # the auth app is an app in django that is used to authenticate and authorize users, 
# I have imported the user model from it
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# This app tracks the objects (generic) that a user likes
# 1 user can like multiple objects



class LikedItem(models.Model): # tells which user liked which object
    user = models.ForeignKey(User, on_delete = models.CASCADE) # if we delete the user, the like disappear
    liked_content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE) # if we delete the object, like disappears
    liked_object_ID = models.PositiveIntegerField() # assuming that the ID is a primary key
    liked_object_type = GenericForeignKey() 