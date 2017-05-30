from django.db import models
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    def __str__(self):              # __unicode__ on Python 2
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):              # __unicode__ on Python 2
        return self.name
class Entry(models.Model):
    blog = models.ForeignKey(Blog,null=True)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(default=0)
    n_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField()
    def __str__(self):              # __unicode__ on Python 2
        return self.headline
