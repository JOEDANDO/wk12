# Generated by Django 5.0.6 on 2024-06-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_player_assists_player_cleansheets_player_goals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opponent', models.CharField(max_length=100)),
                ('hora', models.CharField(max_length=1)),
                ('date', models.CharField(max_length=20)),
                ('lastresult', models.CharField(max_length=100, null=True)),
                ('leagueposition', models.CharField(max_length=5)),
            ],
        ),
    ]