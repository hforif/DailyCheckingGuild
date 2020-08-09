from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'nickname',
            'phone_number',
            'user_image',
            'bio',
        ]