from django.db import models
from django.forms.models import model_to_dict


class Poi(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(decimal_places=7, max_digits=10)
    longitude = models.DecimalField(decimal_places=7, max_digits=10)
    animal_name = models.CharField(max_length=50, null=True, blank=True)
    scientific_name = models.CharField(max_length=50)
    locations = models.CharField(max_length=50)
    feature = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    image = models.ImageField()

    def to_json(self):
        return {
            **model_to_dict(
                self,
                fields=["id", "name", "latitude", "longitude", "animal_name",
                        "scientific_name", "locations", "feature", "slogan", "habitat"]
            ),
            "image_url": self.image.url
        }
