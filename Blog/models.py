from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    data = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
