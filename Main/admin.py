from django.contrib import admin
from .models import Profile,Post,Like,Comment,UserFollowing,Message
# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(UserFollowing)
admin.site.register(Message)