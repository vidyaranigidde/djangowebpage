from django.db import models


"""
class savedata(models.Model):
    planet_name = models.Charfiled(max_length=50)
    rotation_period=models.TextField()
    orbital_period=models.TextField()
    population=models.TextField()
    title_names= models.TextField(null=True)
"""
class Planetss(models.Model):
    name = models.TextField(null = True)

class SaveDataa(models.Model):
    film = models.TextField(null=True) 
    resident = models.TextField(null=True)
    rperiod = models.TextField(null=True)
    operiod = models.TextField(null=True)
    diam = models.TextField(null=True)
    cli = models.TextField(null=True)
    grav = models.TextField(null=True)

