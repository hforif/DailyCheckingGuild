from django.shortcuts import render
from community.models import Profile, Feed
import datetime
import requests

today = datetime.date.today()

# 매일 커밋 여부를 확인하고 Profile에 대한 피드를 생성
def daily_commit(request):
    profile = Profile.objects.get(profile_name='ektmf7890')
    global daily_check_count

    auto_create_commit_feed(profile)

    feed_list = Feed.objects.filter(profile=profile, created_date__date=today)
    return render(request, 'community/daily_commit.html', {'feed_list': feed_list})


#매일 자정에 이 함수가 실행되고 다음 날 자정까지는 이 함수가 실행되지 않게 하려면
# 어떻게 해야할까요?
# 30개의 아이템을 모두 확인하지 않고 처음부터 날짜가 오늘인 값들만 불러올 수는 없나?
def auto_create_commit_feed(profile):
    req = requests.get(f'https://api.github.com/users/{profile.profile_name}/events/public')
    events = req.json()

    global today
    for event in events:
        if event['type']=='PushEvent' and event['created_at'][:10]==str(today):
            commit_url = f"https://github.com/{event['repo']['name']}/commit/{event['payload']['head']}"
            Feed.objects.create(profile=profile,
                                group=profile.group,
                                proof=commit_url)

