from django.forms import ModelForm
from .models import Turn


class TurnForm(ModelForm):
    class Meta:
        model = Turn
        fields = "__all__"
