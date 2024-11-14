from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Project(models.Model):
    project_id = models.IntegerField()
    project_name = models.CharField(verbose_name='Project NAme', max_length=100)
    project_description = models.TextField(verbose_name='Project description')
    project_url = models.URLField()
    project_image = models.URLField()
    project_type = models.CharField(max_length=100)
    project_status = models.CharField(max_length=100)
    project_owner = models.CharField(max_length=100)
    project_owner_email = models.EmailField()
    project_cost_m2 = models.FloatField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.project_name


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_surname = models.CharField(max_length=100, null=True, blank=True)
    contact_phone = models.IntegerField()
    contact_email = models.EmailField()
    contact_message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.contact_name


class Order(models.Model):
    SERVICE_CHOICES = (
        ('Residential Decoration', 'Residential Decoration'),
        ('Ecommercial Decoration', 'Ecommercial Decoration'),
        ('Office Decoration', 'Office Decoration'),
    )
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    date_created = models.DateField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Name


