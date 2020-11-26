from django.contrib import admin
from django.urls import path
from FbDp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "FbDp"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home_view, name='home_view'),
    path('index/',views.index, name='index'),
    path('<int:id>/',views.detail, name='detail'),
    path('<int:id>/',views.delete, name='delete'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)