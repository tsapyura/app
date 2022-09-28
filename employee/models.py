from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64, blank=True, null=True)

    REQUIRED_FIELDS = ["password", "first_name", "last_name"]

    def __str__(self):
        return self.first_name
