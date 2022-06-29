from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User

# 익명게시판 게시글
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # admin site에서 보여지는 모양
    def __str__(self):
        return self.title


# 익명게시판 댓글
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    # admin site에서 보여지는 모양
    def __str__(self):
        return self.comment


# 자유게시판 게시글
class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)

    # admin site에서 보여지는 모양
    def __str__(self):
        return self.title


# 자유게시판 댓글
class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)

    # admin site에서 보여지는 모양
    def __str__(self):
        return self.comment
