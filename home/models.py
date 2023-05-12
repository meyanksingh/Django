from django.db import models

# Create your models here.


class Recipe(models.Model):
    rname = models.CharField(max_length=100)
    rdesc = models.TextField(default='')
    rimg = models.ImageField(upload_to='photos', null=True,blank=True)

    def __str__(self):
        return self.rname