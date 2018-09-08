from django.conf.urls import include, url
from django.contrib import admin

# from posts import posts_home
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include("posts.urls"), name="posts"),
]