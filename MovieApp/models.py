from django.db import models

# Create your models here.
class Movie(models.Model):
    moviename=models.CharField(max_length=50)
    genre=models.CharField(max_length=40)
    releasedate=models.IntegerField()
    rating=models.IntegerField()
    trailer_link = models.URLField(blank=True, null=True)  # ✅ New field for trailer URL

    def __str__(self):
        return self.moviename

    
    
