
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
	def test_create_team(self):
		team = Team.objects.create(name="Marvel", description="Team Marvel")
		self.assertEqual(str(team), "Marvel")

	def test_create_user(self):
		team = Team.objects.create(name="DC", description="Team DC")
		user = User.objects.create(email="batman@dc.com", name="Batman", team=team)
		self.assertEqual(str(user), "batman@dc.com")

	def test_create_workout(self):
		workout = Workout.objects.create(name="Pushups", description="Upper body", suggested_for="Marvel")
		self.assertEqual(str(workout), "Pushups")

	def test_create_activity(self):
		team = Team.objects.create(name="X-Men", description="Mutants")
		user = User.objects.create(email="logan@xmen.com", name="Logan", team=team)
		workout = Workout.objects.create(name="Run", description="Cardio")
		activity = Activity.objects.create(user=user, workout=workout, date="2025-12-17", duration_minutes=30, points=10)
		self.assertEqual(activity.points, 10)

	def test_create_leaderboard(self):
		team = Team.objects.create(name="Avengers", description="Earth's Mightiest Heroes")
		leaderboard = Leaderboard.objects.create(team=team, total_points=100)
		self.assertEqual(str(leaderboard), "Avengers - 100")
