from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Game(models.Model):
    gameTitle = models.CharField(max_length = 200)
    gameDate = models.DateField()
    gameRating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
