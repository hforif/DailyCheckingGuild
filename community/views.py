from django.shortcuts import render
from community.models import Profile, Feed


# 매일 정각에 커밋 여부를 확인하고 Profile에 대한 피드를 생성
# feed_list = Feed.objects.filter(profile=profile)
def daily_commit(request):
    profile = Profile.objects.get(profile_name='developer_yun')

    return render(request, 'community/daily_commit.html')