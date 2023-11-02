from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    profile_img = models.ImageField(default='profile_picture\default.jpg', upload_to='profile_picture')
    country_code = models.CharField(max_length=5, default=None, blank=True, null=True)
    phone = models.CharField(max_length=15, default=None, blank=True, null=True)
    dob = models.DateField(default=None, blank=True, null=True)
    fav_mov = models.TextField(default=None, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile "