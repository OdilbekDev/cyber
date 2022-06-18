from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *


urlpatterns = [
    path('info/', Info_get),
    path('menu/', Menu_get),
    path('image/', Image_get),
    path('introductory_section/', Introductory_section_get),
    path('our_mission/', Our_missions_get),
    path('games/', Games_get),
    path('last_turnir/',Last_Turnir_get),
    path('strimes/', Strimes_get),
    path('team_one_player/', Team_one_playerView),
    path('team/',Team_post),
    path('news/', New_Letter_post),
    path('random_team/<int:pk>/', Random_Team),
    path('random_team_one/<int:pk>/', Random_Team_One),
    path('turnir/filter/<int:pk>/', FilterTurnir),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)