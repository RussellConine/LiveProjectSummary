from django.db import models


TERRAIN_TYPES = [("All-Mountain", "All-Mountain"),
                 ("Freestyle", "Freestyle"),
                 ("Carving", "Carving"),
                 ("Powder", "Powder")]


class Ski(models.Model):
    brand = models.CharField(max_length=100)
    ski_model = models.CharField(max_length=30)
    ski_length = models.IntegerField()
    ski_width = models.IntegerField()
    terrain = models.CharField(max_length=30, choices=TERRAIN_TYPES)
    color = models.CharField(max_length=50, verbose_name='Color/Design')

    Skis = models.Manager()

    def __str__(self):
        return self.brand + ' ' + self.ski_model + ' ' + str(self.ski_length) + 's'


