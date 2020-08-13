from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_job
import requests, datetime
from community.models import Feed, Profile
from django.conf import settings

scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)


def auto_create_commit_feed():
    profile = Profile.objects.get(profile_name='ektmf7890')
    req = requests.get(f'https://api.github.com/users/{profile.profile_name}/events/public')
    events = req.json()

    today = str(datetime.date.today())

    for event in events:
        if event['type']=='PushEvent' and event['created_at'][:10]== today:
            commit_url = f"https://github.com/{event['repo']['name']}/commit/{event['payload']['head']}"
            Feed.objects.create(profile=profile,
                                group=profile.group,
                                proof=commit_url)


def start():
    scheduler.add_job(auto_create_commit_feed, 'cron', hour=0, replace_existing=True, id='auto_create_commit_feed')
    scheduler.start()