from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date_time = models.DateTimeField()
    blog_body = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

