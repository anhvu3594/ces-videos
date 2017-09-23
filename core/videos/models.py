# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Video(models.Model):
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	desciption = models.CharField(max_length=1000)