from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date_time = models.DateTimeField()
    blog_body = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.blog_body[:100]

    def pub_date_pretty(self):
        return self.pub_date_time.strftime('%b %e %Y')