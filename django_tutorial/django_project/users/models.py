from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        maxSize = 256
        if img.height > maxSize or img.width > maxSize:
            output_size = (maxSize, maxSize)
            img.thumbnail(output_size)
            img.save(self.image.path)
