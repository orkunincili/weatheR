from django.db import models

# Create your models here.



class Weather(models.Model):

    degree=models.FloatField()
    day=models.DateTimeField()



    def __str__(self):

        return self.degree


