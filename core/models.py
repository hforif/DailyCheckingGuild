from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 사용자
class User(AbstractUser):
    nickname = models.CharField(max_length=10, default='unknown')
    phone_number = models.CharField(max_length=20)
    user_image = models.ImageField(upload_to='account/user', blank=True, null=True, default=None)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

    def get_username(self):
        return self.username


# 인증 그룹
class Group(models.Model):
    group_name = models.CharField(max_length=30, unique=True)
    group_code = models.CharField(max_length=30)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, through='Profile')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.group_name


# 그룹에서 사용하는 프로필
class Profile(models.Model):
    profile_name = models.CharField(max_length=10, null=True)
    STATUS_CHOICES = (
        ('g', 'invite'),  # 그룹에서 유저에게 초대
        ('u', 'request'),  # 유저가 그룹으로 가입요청
        ('a', 'accepted'),  # 유저가 그룹에서 활동중
        ('r', 'refused')  # 유저의 요청을 그룹에서 거절
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# 인증
class Feed(models.Model):
    profile = models.ForeignKey(Profile, default='알 수 없음', on_delete=models.SET_DEFAULT)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_date = 0


# 인증에 달 수 있는 댓글
class Comment(models.Model):
    text = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default='알 수 없음', on_delete=models.SET_DEFAULT)


# 불량 인증에 대한 신고
class Report(models.Model):
    target = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_date = 0


# 신고에 대한 사유서 or 호소문 or 변명 or 기타 등등
class Appeal(models.Model):
    target = models.ForeignKey(Feed, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = 0


# 벌금
class Fine(models.Model):
    target = models.ForeignKey(Feed, on_delete=models.CASCADE)
    money = models.IntegerField()


# 유저에게 가는 메세지
class Message(models.Model):
    target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    sender = models.CharField(max_length=30)
