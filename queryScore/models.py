from django.db import models

# Create your models here.
# The model for User table


class User(models.Model):
    number = models.CharField(max_length=40, primary_key=True)
    name = models.CharField(max_length=40)
    CET46exam = models.CharField(max_length=15, blank=True)
    NEEPexam = models.CharField(max_length=15, blank=True)
    PSCexam = models.CharField(max_length=13, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.number
