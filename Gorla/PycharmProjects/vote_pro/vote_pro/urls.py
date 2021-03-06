from django.contrib import admin
from django.urls import path
from vote_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index, name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/',views.results, name='results'),
    path('<int:question_id>/vote/',views.vote, name='vote'),
]
