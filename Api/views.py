from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from Api.models import *
from Api.serializer import *
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@api_view(['GET'])
def Info_get(request):
    a = Info.objects.all().order_by('-id')[0:1]
    ser = InfoSerializer(a,many=True)
    return Response(ser.data)

@api_view(['GET'])
def Menu_get(request):
    a = Menu.objects.all()
    ser = MenuSerializer(a,many=True)
    return Response(ser.data)

@api_view(['GET'])
def Image_get(request):
    a = Img_Gallery.objects.all()
    ser = ImageSerializer(a,many=True)
    return Response(ser.data)



@api_view(['GET'])
def Introductory_section_get(request):
    a = Introductory_section.objects.all().order_by('-id')[0:1]
    ser = IntroductorySerializer(a,many=True)
    return Response(ser.data)



@api_view(['GET'])
def Our_missions_get(request):
    a = Our_Missions.objects.all()
    ser = OurSerializer(a,many=True)
    return Response(ser.data)




@api_view(['GET'])
def Games_get(request):
    a = Games.objects.all()
    ser = GameSerializer(a,many=True)
    return Response(ser.data)

@api_view(['GET'])
def Last_Turnir_get(request):
    a = Turnir.objects.all()
    ser = LastTurnirSerializer(a,many=True)
    return Response(ser.data)

@api_view(['GET'])
def Strimes_get(request):
    a = Strimes.objects.all()
    ser = StrimesSerializer(a,many=True)
    return Response(ser.data)



@api_view(['POST'])
def Team_one_playerView(request):
    name = request.POST.get('name') 
    img_team = request.FILES.get('img_team')
    An_experience_1 = request.POST.get('An_experience_1')
    An_experience_2 = request.POST.get('An_experience_2')
    Surname = request.POST.get('Surname')
    Directions = request.POST.get('Directions')
    Email = request.POST.get('Email')
    Phone_Number = request.POST.get('Phone_Number')
    game = request.POST.get('game')

    a = Team_one_player.objects.create(name=name, 
    img_team=img_team, 
    An_experience_1=An_experience_1, An_experience_2=An_experience_2,
    Surname=Surname, Directions=Directions,
    Email=Email, game_id=game,Phone_Number=Phone_Number)
    b = Team_one_player.objects.all().order_by('-id')
    ser = Team_oneSerializer(b,many=True)
    return Response(ser.data)



@api_view(['POST'])
def Team_post(request):
    name = request.POST.get('name') 
    img_team = request.FILES.get('img_team')
    An_experience_1 = request.POST.get('An_experience_1')
    An_experience_2 = request.POST.get('An_experience_2')
    Number_Player = request.POST.get('Number_Player')
    Directions = request.POST.get('Directions')
    Email = request.POST.get('Email')
    Phone_Number = request.POST.get('Phone_Number')
    game = request.POST.get('game')
    a= Team.objects.create(name=name, img_team=img_team, An_experience_1=An_experience_1, An_experience_2=An_experience_2, Number_Player=Number_Player, Directions=Directions, Email=Email, Phone_Number=Phone_Number, game_id=game )
    b = Team.objects.all().order_by('-id')
    ser = TeamSerializer(b, many=True)

    return Response(ser.data)

@api_view(['POST'])
def New_Letter_post(request):
    email= request.POST.get('email')
    a = News_Letter.objects.create(email=email)
    b = News_Letter.objects.all().order_by('-id')
    ser = NewsSerializer(b, many=True)
    return Response(ser.data)


import random

@api_view(['GET'])
def Random_Team(request,pk):
    users = list(Team.objects.filter(game__id=pk))

    data = {}
    for i in range(int(len(users)/2)):
        team = random.sample(users, k=2)
        data[team[0].name] = str(team[1].name)
        for e in team:
            print(data)
            users.remove(e)
    return Response(data)


@api_view(['GET'])
def Random_Team_One(request,pk):
    player = list(Team_one_player.objects.filter(game__id=pk))
    data = {}
    for i in range(int(len(player)/2)):
        team = random.sample(player, k=2)
        data[team[0].name] = str(team[1].name)
        print(data[team[0]])
        for e in team:
            player.remove(e)
        
        
    return Response(data)


@api_view(['GET'])
def FilterTurnir(request, pk):
    game = Games.objects.get(id=pk)
    turnir = Turnir.objects.get(game=game)
    ser = LastTurnirSerializer(turnir)
    return Response(ser.data)


@api_view(['GET'])
def FilterOneVsOne(request, pk):
    game = Games.objects.get(id=pk)
    turnir = One_Vs_One.objects.get(game=game)
    ser = OneVsOneSerializer(turnir)
    return Response(ser.data)


def Login_funk(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        login = list(Login.objects.all())
        for i in login:
            if username == i.username and password == i.password:
                print(True)
                return redirect('admin')
            else:print(False)
    return render(request, 'index.html')
@api_view(['DELETE', 'POST','GET','PUT'])
def Admin_Page(request):
     
    return render(request, 'table-basic.html')