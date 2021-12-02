from django.db import models


# Create your models here.


class Admin (models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    institute = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    even_date = models.DateField()
    registration_last_date = models.DateField()
    duration = models.DurationField()
    price = models.IntegerField()
    place = models.CharField(max_length=200)
    visits = models.IntegerField(default=0)
    link = models.CharField(max_length=200, default="")
    admin = models.ForeignKey(
        Admin, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
