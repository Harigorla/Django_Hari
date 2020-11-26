from django.shortcuts import render

from myapp2.forms import ProfileForm
from myapp2.models import Profile


def SaveProfile(request):
    saved = False

    if request.method == "POST":
        # Get the posted form
        MyProfileForm = ProfileForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Profile()
            profile.name = MyProfileForm.cleaned_data["name"]
            profile.picture = MyProfileForm.cleaned_data["picture"]
            profile.save()
            saved = True
    else:
        MyProfileForm = ProfileForm()

    return render(request, 'saved.html', locals())
