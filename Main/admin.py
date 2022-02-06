from django.contrib import admin
from .models import Profile,Post,Like,Project_tag,project_comment,Comment,like_project,UserFollowing,Message,Project,collab,notification
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
admin.site.register(like_project)
admin.site.register(project_comment)
admin.site.register(Project_tag)