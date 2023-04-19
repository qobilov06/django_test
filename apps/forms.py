from apps.models import Users
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'password1')
