

from djongo import models

class Team(models.Model):
	id = models.ObjectIdField(primary_key=True, editable=False)
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)
	def __str__(self):
		return self.name

class User(models.Model):
	id = models.ObjectIdField(primary_key=True, editable=False)
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=100)
	team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
	def __str__(self):
		return self.email

class Workout(models.Model):
	id = models.ObjectIdField(primary_key=True, editable=False)
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	suggested_for = models.CharField(max_length=100, blank=True)
	def __str__(self):
		return self.name

class Activity(models.Model):
	id = models.ObjectIdField(primary_key=True, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	workout = models.ForeignKey(Workout, on_delete=models.SET_NULL, null=True)
	date = models.DateField()
	duration_minutes = models.PositiveIntegerField()
	points = models.PositiveIntegerField(default=0)
	def __str__(self):
		return f"{self.user.email} - {self.workout.name} ({self.date})"

class Leaderboard(models.Model):
	id = models.ObjectIdField(primary_key=True, editable=False)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	total_points = models.PositiveIntegerField(default=0)
	last_updated = models.DateTimeField(auto_now=True)
	def __str__(self):
		return f"{self.team.name} - {self.total_points}"
