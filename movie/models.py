from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('Action','ACTION'),
    ('Drama','DRAMA'),
    ('Comedy','COMEDY'),
    ('Romance','ROMANCE'),
)

LANGUAGE_CHOICES=(
    ('English','ENGLISH'),
    ('Hindi','HINDI'),
)

STATUS_CHOICES = (
    ('RA','RECENTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED'),
)

LINK_CHOICES =(
    ('D','DOWNLOAD LINK'),
    ('W','WATCH LINK'),
    
)

class Movie(models.Model):
    title = models.CharField(max_length =100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    link =models.CharField(choices=LINK_CHOICES, max_length = 1)
    # cast = models.CharField(max_length=100)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    
    
    def __str__(self):  
        return self.title
    
LINK_CHOICES ={
    ('D','DOWNLOAD LINK'),
    ('W','WATCH LINK'),
}    
class Movielinks(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length = 1)
    link = models.URLField()
    
    def __str__(self):
        return str(self.movie)
    

