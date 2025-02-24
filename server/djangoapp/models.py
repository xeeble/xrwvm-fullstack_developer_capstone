from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCH', 'Hatchback'),
        ('COUPE', 'Coupe'),
        ('SPORT', 'Sports car'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[MaxValueValidator(2023),
                    MinValueValidator(2015)
        ])
    mileage = models.IntegerField(default=0)
    
    def __str__(self):
        return "Name: " + self.name + "," + \
                "Car Make: " + str(self.car_make) + "," + \
                "Car Type: " + self.type + "," + \
                "Year: " + str(self.year)
