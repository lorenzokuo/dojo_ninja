from __future__ import unicode_literals
from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    def __repr__(self):
        return "<Blog object: {} {}>".format(self.name, self.city, self.state)

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)