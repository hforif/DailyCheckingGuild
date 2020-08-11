from django.shortcuts import render
from community.models import Profile, Feed
import datetime

today = datetime.date.today()


# 매일 커밋 여부를 확인하고 Profile에 대한 피드를 생성
def daily_commit(request):
    profile = Profile.objects.get(profile_name='developer_yun')
    feed_list = Feed.objects.filter(profile=profile, created_date__date=today)

    return render(request, 'community/daily_commit.html', {'feed_list': feed_list})