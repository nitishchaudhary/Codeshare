from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic  =  models.ImageField(default = 'default.jpg',upload_to = 'profile_images')
    about = models.TextField()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Post(models.Model):
    user_name = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.CharField(max_length=255)
    img = models.ImageField(upload_to = 'post_images')
    date_posted = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return reverse('post-detail' , kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post ,related_name = 'details' ,on_delete=models.CASCADE)
    username = models.ForeignKey(User ,related_name = 'details' ,on_delete=CASCADE)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(default = timezone.now)

class Like(models.Model):
    user = models.ForeignKey(User , related_name = 'likes' ,on_delete=CASCADE )
    post  = models.ForeignKey(Post , related_name = 'likes' , on_delete=CASCADE)