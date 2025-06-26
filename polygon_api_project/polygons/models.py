from django.db import models

class PolygonRegion(models.Model):
    name = models.CharField(max_length=100)
    points = models.TextField(help_text="List of coordinates as JSON string: [[x1, y1], [x2, y2], ...]")

    def __str__(self):
        return self.name
