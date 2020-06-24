from django.db import models


class Blog(models.Model):
    post_title = models.CharField(max_length=200)
    post_contents = models.TextField()
    post_image = models.ImageField(upload_to='blogs_images')
    # post_owner = models.ForeignKey('', on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
