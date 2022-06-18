from django.db import models

# Create your models here.
class Info(models.Model):
    logo  = models.ImageField(upload_to='info/')
    facebook = models.URLField()
    Telegram = models.URLField()
    Instagram = models.URLField()
    YouTube = models.URLField()

class Menu(models.Model):
    text  = models.CharField(max_length=255)

class Introductory_section(models.Model):
    text = models.CharField(max_length=255)


class Our_Missions(models.Model):
    img = models.ImageField(upload_to='our_missions/')
    title = models.CharField(max_length=255)
    text = models.TextField()

class Games(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
class Team_one_player(models.Model):
    name = models.CharField(max_length=255)
    img_team = models.ImageField(upload_to='Image_Team_One_Player/')
    An_experience_1 = models.IntegerField()
    An_experience_2 = models.IntegerField()
    Surname = models.CharField(max_length=255)
    Directions = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=255)
    game = models.ForeignKey(Games,on_delete=models.CASCADE)

class Team(models.Model):
    name = models.CharField(max_length=255)
    img_team = models.ImageField(upload_to='Image_Team_One_Player/')
    An_experience_1 = models.IntegerField()
    An_experience_2 = models.IntegerField()
    Number_Player = models.CharField(max_length=255)
    Directions = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=255)
    game = models.ForeignKey(Games,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Turnir(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='team_1')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateTimeField()
    game = models.ForeignKey(Games, on_delete=models.CASCADE)


class One_Vs_One(models.Model):
    user1 = models.ForeignKey(Team_one_player, on_delete=models.CASCADE,related_name='user1')
    user2 = models.ForeignKey(Team_one_player, on_delete=models.CASCADE)
    date =models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)


class Img_Gallery(models.Model):
    imgages = models.ImageField(upload_to='Image_Gallery/')


class Strimes(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=255)


class News_Letter(models.Model):
    email = models.EmailField()
    

class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
