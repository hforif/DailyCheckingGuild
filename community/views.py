from django.shortcuts import render
from community.models import Profile, Feed
import datetime

today = datetime.date.today()


def daily_commit(request):
    profile = Profile.objects.get(profile_name='ektmf7890')
    feed_list = Feed.objects.filter(profile=profile, created_date__date=today)
    return render(request, 'community/daily_commit.html', {'feed_list': feed_list})





