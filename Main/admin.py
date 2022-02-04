from django.contrib import admin
from .models import Profile,Post,Like,Comment,UserFollowing,Message,Project,collab,notification
# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(UserFollowing)
admin.site.register(Message)
admin.site.register(Project)
admin.site.register(collab)
admin.site.register(notification)