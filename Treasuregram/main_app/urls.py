from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:treasure_id>/', views.details, name = 'detail'),
    path('post_url/$', views.post_treasure, name = 'post_treasure'),
    path('user/<username>/', views.profile, name = 'profile'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('like_treasure/', views.like_treasure, name = 'like_treasure'),
]

#Add to the bottom of your file
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

