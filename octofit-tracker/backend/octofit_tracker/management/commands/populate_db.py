
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Limpar coleções diretamente no MongoDB
        db = connection.cursor().db_conn
        db['octofit_tracker_user'].drop()
        db['octofit_tracker_team'].drop()
        db['octofit_tracker_workout'].drop()
        db['octofit_tracker_activity'].drop()
        db['octofit_tracker_leaderboard'].drop()

        # Criar times
        marvel = Team.objects.create(name='Marvel', description='Team Marvel')
        dc = Team.objects.create(name='DC', description='Team DC')

        # Criar usuários
        tony = User.objects.create(email='tony@marvel.com', name='Tony Stark', team=marvel)
        steve = User.objects.create(email='steve@marvel.com', name='Steve Rogers', team=marvel)
        bruce = User.objects.create(email='bruce@dc.com', name='Bruce Wayne', team=dc)
        diana = User.objects.create(email='diana@dc.com', name='Diana Prince', team=dc)

        # Criar workouts
        run = Workout.objects.create(name='Run', description='Cardio', suggested_for='Marvel')
        pushups = Workout.objects.create(name='Pushups', description='Upper body', suggested_for='DC')

        # Criar atividades
        Activity.objects.create(user=tony, workout=run, date=timezone.now().date(), duration_minutes=30, points=10)
        Activity.objects.create(user=steve, workout=pushups, date=timezone.now().date(), duration_minutes=20, points=8)
        Activity.objects.create(user=bruce, workout=run, date=timezone.now().date(), duration_minutes=25, points=9)
        Activity.objects.create(user=diana, workout=pushups, date=timezone.now().date(), duration_minutes=15, points=7)

        # Criar leaderboard
        Leaderboard.objects.create(team=marvel, total_points=18)
        Leaderboard.objects.create(team=dc, total_points=16)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
