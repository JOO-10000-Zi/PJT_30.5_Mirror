from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    shop_number = models.CharField(max_length=80)
    between_pay = models.CharField(max_length=80)
    opening_time = models.CharField(max_length=80)
    break_day = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    tag2 = models.TextField()
    tag2 = models.TextField()
    tag2 = models.TextField()
    tag2 = models.TextField()
    tag2 = models.TextField()
