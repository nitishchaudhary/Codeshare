from datetime import date
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
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
    user_name = models.ForeignKey(User, related_name="post",on_delete = models.CASCADE)
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
    
class UserFollowing(models.Model):
    user_id = models.ForeignKey(User , related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(User , related_name="followers",on_delete=models.CASCADE)

class Message(models.Model):
    sender_id = models.ForeignKey(User,related_name="sender",on_delete=models.CASCADE)
    reciever_id = models.ForeignKey(User,related_name="receiver",on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    mesage_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to = 'message_media',blank=True)

class Project(models.Model):
    author_id = models.ForeignKey(User,related_name="project",on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=255 , blank=True)
    project_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to = 'project_media',blank=True)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('project-detail' , kwargs={'pk':self.pk})

class Project_tag(models.Model):
    project = models.ForeignKey(Project,related_name='tag',on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)
    

class collab(models.Model):
    project_id = models.ForeignKey(Project,related_name='collab_request',on_delete=models.CASCADE)
    requesting_user = models.ForeignKey(User,related_name="requesting_user",on_delete=models.CASCADE)
    requested_user = models.ForeignKey(User,related_name='requested_user',on_delete=models.CASCADE)

class notification(models.Model):
    user_id = models.ForeignKey(User,related_name="notification",on_delete=models.CASCADE)
    notification_message = models.TextField(default=None)
    read = models.BooleanField(default=False)
    notification_time = models.DateTimeField(default=timezone.now())

class like_project(models.Model):
    user_id = models.ForeignKey(User,related_name='project_likes',on_delete=models.CASCADE)
    project = models.ForeignKey(Project,related_name='likes',on_delete=models.CASCADE)

class project_comment(models.Model):
    user_id = models.ForeignKey(User,related_name='project_comments',on_delete=models.CASCADE)
    project = models.ForeignKey(Project,related_name="comments",on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(default=timezone.now())