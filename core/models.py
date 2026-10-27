from django.db import models

class Wigs(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    type = models.CharField(max_length=200)
    colour = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    length = models.CharField(max_length=50)

    def __str__(self):
        return self.name