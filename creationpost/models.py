from django.db import models
from taggit.managers import TaggableManager
class Post(models.Model):
    title = models.CharField(max_length=45)
    content = models.TextField()
    pub_date=models.DateTimeField(auto_now=True,null=True)
    image=models.ImageField(upload_to='images/', null=True, default='media/images/no_image.png')
    tags=TaggableManager()
    def __str__(self):
        return '{}'.format(self.title)

# Create your models here.
