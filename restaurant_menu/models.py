from django.db import models


# Create your models here.
class RestaurantMenu(models.Model):
    restaurant_name = models.CharField(max_length=64)
    menu1 = models.TextField()
    menu2 = models.TextField()
    menu3 = models.TextField()
    menu4 = models.TextField()
    menu5 = models.TextField()
    menu6 = models.TextField()
    menu7 = models.TextField()
    ratind = models.FloatField()

    def __str__(self):
        return self.restaurant_name
