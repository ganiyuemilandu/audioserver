from django.urls import path
from .views import SongList, SongDetail
from .views import PodcastList, PodcastDetail
from .views import AudiobookList, AudiobookDetail

urlpatterns = [
    path('song/<int:pk>/', SongDetail.as_view(), name='song_list'),
    path('song/', SongList.as_view()),
    path('podcast/<int:pk>/', PodcastDetail.as_view()),
    path('podcast/', PodcastList.as_view()),
    path('audiobook/<int:pk>/', AudiobookDetail.as_view()),
    path('audiobook/', AudiobookList.as_view()),
]