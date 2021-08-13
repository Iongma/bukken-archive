from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'
urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('likes/<int:pk>', views.LikesView.as_view(), name='likes'),
]

# ローカルでmediaファイルを扱う場合の処理
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
