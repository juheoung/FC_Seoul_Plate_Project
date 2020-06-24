from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    post_title = models.CharField(null=False, max_length=200)
    post_contents = models.TextField(null=False)
    post_image = models.ImageField(upload_to='')
    post_owner = models.ForeignKey(User, default='', null=False, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
