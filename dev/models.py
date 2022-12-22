from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
# Create your models here.


class about(models.Model):
    degree = models.CharField(max_length=30)
    year_of_birth = models.DateField()
    year_of_programming = models.DateField()
    work = models.PositiveIntegerField()

    def __str__(self):
        return self.degree


class work(models.Model):
    title = models.CharField(max_length=200)
    fullabout = models.TextField()
    photo = models.ImageField(upload_to="works/", blank=True, null=True)
    workurl = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title


class skill(models.Model):
    name = models.CharField(max_length=200)
    level = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

