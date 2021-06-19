from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    arcana = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.user.username} Profile, with Arcana {self.arcana}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if(img.height > 640 or img.width > 640):
            output_size = (640, 640)
            img.thumbnail(output_size)
            img.save(self.image.path)