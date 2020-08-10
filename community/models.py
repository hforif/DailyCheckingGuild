from django.db import models
from django.conf import settings

# Create your models here.


# 인증 그룹
class Group(models.Model):
    group_name = models.CharField(max_length=30, unique=True)
    group_code = models.CharField(max_length=30, unique=True)
    bio = models.TextField(blank=True, default='')
    master = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='master_group_set')
    member = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Profile', related_name='member_group_set')

    def __str__(self):
        return self.group_name


# 그룹에서 사용하는 프로필
class Profile(models.Model):
    profile_name = models.CharField(max_length=20, null=True)
    STATUS_CHOICES = (
        ('g', 'invite'),  # 그룹에서 유저에게 초대
        ('u', 'request'),  # 유저가 그룹으로 가입요청
        ('a', 'accepted'),  # 유저가 그룹에서 활동중
        ('r', 'refused'),  # 유저의 요청을 그룹에서 거절
        ('b', 'block')  # 유저가 그룹의 요청을 차단
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    bio = models.TextField(blank=True, default='')  # 유저의 목표에 대한 설명

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


# 인증
class Feed(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    proof = models.FileField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)


