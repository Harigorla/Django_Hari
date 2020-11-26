from django.forms import ModelForm
from .models import WallPaper

class WallForm(ModelForm):
    class Meta:
        model = WallPaper
        fields = "__all__"