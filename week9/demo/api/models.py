from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField(default='')
    count = models.IntegerField()

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count
        }

class Category(models.Model):
    name = models.CharField(max_length=300)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name
        }
# Create your models here.
