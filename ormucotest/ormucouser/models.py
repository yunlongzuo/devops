# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    f_color = models.CharField(max_length=11)
    f_animal = models.CharField(max_length=5)

    def __str__(self):
        return self.name
