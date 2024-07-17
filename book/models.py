from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    title = models.CharField(max_length=35, blank=False, null=False)
    description = models.TextField(max_length=255, blank=False, null=False)
    rating = models.FloatField(blank=False, null=False, default=0.0)
    publish_date = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.author} (Rating: {self.rating})"