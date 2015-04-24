# -*- coding: utf-8 -*-
from django.db import models

class TopSection(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "TopSection"
        verbose_name_plural = "TopSections"

    def __str__(self):
        return self.name
    