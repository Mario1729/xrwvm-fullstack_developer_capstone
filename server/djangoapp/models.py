from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    # Many-to-One relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('CRV', 'CRV'),
        ('MUV', 'MUV'),
        # Add more choices as required
    ]
    car_type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default='SUV',
    )
    year = models.IntegerField(
        default=now().year,
        validators=[
            MaxValueValidator(now().year),
            MinValueValidator(2015)
        ]
    )
    # Refers to a dealer in Cloudant database
    dealer_id = models.IntegerField()
    mileage = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.car_make.name})"
