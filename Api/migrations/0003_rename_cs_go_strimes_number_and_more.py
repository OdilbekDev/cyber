# Generated by Django 4.0.4 on 2022-06-15 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_last_turnir_team_2_alter_last_turnir_team_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='strimes',
            old_name='Cs_Go',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='strimes',
            name='Pubg_Sitrim',
        ),
        migrations.RemoveField(
            model_name='strimes',
            name='Strimers',
        ),
        migrations.RemoveField(
            model_name='strimes',
            name='Twitch_Sitrim',
        ),
        migrations.AddField(
            model_name='strimes',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
