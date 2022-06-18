
from .models import *
from rest_framework import serializers


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'



class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img_Gallery
        fields = '__all__'


class LastTurnirSerializer(serializers.ModelSerializer):
    class Meta:
        depth=1
        model = Turnir
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Letter
        fields = '__all__'


class OurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_Missions
        fields = '__all__'


class StrimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strimes
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class Team_oneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_one_player
        fields = '__all__'

class IntroductorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Introductory_section
        fields = '__all__'




class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = '__all__'


class OneVsOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = '__all__'