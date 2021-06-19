from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'
urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('home', views.HomeView.as_view(), name='home'),
    # path('user', views.IndexView.as_view(), name='user'),
    # path('user/like', views.IndexView.as_view(), name='user_like'),

    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]

# ローカルでmediaファイルを扱う場合の処理
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
