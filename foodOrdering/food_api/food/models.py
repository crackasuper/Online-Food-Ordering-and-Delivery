from django.db import models

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=255)
    food_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.food_name

class Delivery(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class User(models.Model): # renamed from 'user' to avoid conflicts
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName

class OrderFood(models.Model):
    userName = models.CharField(max_length=255)
    foodName = models.CharField(max_length=255)
    items = models.IntegerField()

    def __str__(self):
        return f"{self.userName} ordered {self.foodName}"

class Admin(models.Model):
    firstName = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName