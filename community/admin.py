from django.contrib import admin
from community.models import Group, Feed, Profile

# Register your models here.

admin.site.register(Group)
admin.site.register(Profile)
admin.site.register(Feed)

