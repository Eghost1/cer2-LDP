from django.db import models

class Number(models.Model):
    number = models.IntegerField()
    letter = models.CharField()

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    pokedex_number = models.IntegerField()
    primary_type = models.CharField(max_length=15)
    secondary_type = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(blank='',default='',upload_to='imagenes/')
    def __str__(self):
        return self.name