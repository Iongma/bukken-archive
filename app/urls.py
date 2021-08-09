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
    path('like/', views.LikesView.as_view(), name='like'),

    # path('user_create/', views.UserCreate.as_view(), name='user_create'),
    # path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    # path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
    # path('likes/<int:pk>/', views.LikesView.as_view(), name='likes'),
]

# ローカルでmediaファイルを扱う場合の処理
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
