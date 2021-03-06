# Generated by Django 4.0.4 on 2022-06-16 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_rename_cs_go_strimes_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='One_Vs_One',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.games')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='Api.team_one_player')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.team_one_player')),
            ],
        ),
        migrations.CreateModel(
            name='Turnir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.games')),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1', to='Api.team')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.team')),
            ],
        ),
        migrations.DeleteModel(
            name='Last_Turnir',
        ),
    ]
