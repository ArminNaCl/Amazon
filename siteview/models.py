from django.db import models

# Create your models here.
class SlideShow(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='media/slideshow/')
    action_text = models.CharField(max_length=20,default='shop now') 
    action_url = models.URLField(default="http://127.0.0.1:8000")

    def __str__(self):
        return self.title