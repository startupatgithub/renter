import datetime

from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='%(class)s_building')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Renter(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='%(class)s_room')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    whatsapp = models.CharField(max_length=100, null=True, blank=True)
    agreement_start = models.DateTimeField(null=True, blank=True)
    agreement_end = models.DateTimeField(null=True, blank=True)
    advance = models.DecimalField(max_digits=100, decimal_places=5)
    rent = models.DecimalField(max_digits=100, decimal_places=5)

    def __str__(self):
        return self.name


class Rent(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE, related_name='%(class)s_renter')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=5)
    balance = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    date = models.DateTimeField(auto_now=True)
    pay_for = models.DateField()

    def is_paid(self):
        return self.balance == 0

    def __str__(self):
        return self.renter.name
