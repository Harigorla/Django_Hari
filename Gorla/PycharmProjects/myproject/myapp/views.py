from django.shortcuts import render
from .models import POST
from .forms import PostForm


def SaveProfile(request):
    if request.method == "POST":
        MyProfileForm = PostForm(request.POST, request.FILES)
        if MyProfileForm.is_valid():
            profile = POST()
            profile.title = MyProfileForm.cleaned_data["title"]
            profile.header_image = MyProfileForm.cleaned_data['header_image']
            profile.post_date = MyProfileForm.cleaned_data['post_date']
            profile.save()
    else:
        MyProfileForm = PostForm()
    return render(request, 'saved.html', locals())