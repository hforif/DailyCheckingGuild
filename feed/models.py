from django.db import models
from community.models import Feed
from django.conf import settings

# Create your models here.


# 인증에 달 수 있는 댓글
class Comment(models.Model):
    text = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)


# 불량 인증에 대한 신고
class Report(models.Model):
    target = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)


# 신고에 대한 사유서 or 호소문 or 변명 or 기타 등등
class Appeal(models.Model):
    target = models.ForeignKey(Feed, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True)


# 벌금
class Fine(models.Model):
    target = models.ForeignKey(Feed, on_delete=models.CASCADE)
    money = models.IntegerField()


# 유저에게 가는 메세지
class Message(models.Model):
    target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    sender = models.CharField(max_length=30)
