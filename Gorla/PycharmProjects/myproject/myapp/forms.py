from django.forms import ModelForm
from .models import POST


class PostForm(ModelForm):
    class Meta:
        model = POST
        fields = "__all__"
