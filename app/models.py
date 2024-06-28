from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(10),
        ])
    message = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name

# from mongoengine import Document, fields

# class Contact(Document):
#     name = fields.StringField(required=True)
#     email = fields.EmailField(required=True) 
#     number = fields.IntField(required=True)
#     message = fields.StringField(required=True)
