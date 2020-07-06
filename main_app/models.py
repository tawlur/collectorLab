from django.db import models
from django.urls import reverse

# A tuple of 2-tuples
GALLONS = (
    ('1', '1 Gallons'),
    ('5', '5 Gallons'),
    ('F', 'Fill it up!')
)

class Driver(models.Model):
  name = models.CharField(max_length=50)
  skill = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('drivers_detail', kwargs={'pk': self.id})

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    drivers = models.ManyToManyField(Driver)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})


class Fueling(models.Model):
  date = models.DateField('fueling date')
  gallons = models.CharField(
    max_length=1,
	choices=GALLONS,
	default=GALLONS[0][0]
  )
  # Create a car_id FK
  car = models.ForeignKey(Car, on_delete=models.CASCADE)
  
  def __str__(self):
        return f"{self.get_gallons_display()} on {self.date}"
    
  class Meta:
        ordering = ['-date']