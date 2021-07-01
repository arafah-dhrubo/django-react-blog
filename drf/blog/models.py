from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=500)
    image=models.ImageField(upload_to="blog-image/")
    post=models.CharField(max_length=10000)
    created=models.DateField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
