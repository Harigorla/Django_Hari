from django.db import models


class WallPaper(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
