from django.test import TestCase
from django.contrib.auth.models import User

from ..activities import create, get_newsfeed, get_activities
from ..connections import follow

class ActivitiesTest(TestCase):

	def setUp(self):
		self.me = User.objects.create_user(
			username="mohamed",
			email="turkipro@gmail.com"
		)

		self.you = User.objects.create_user(
			username="yourusername",
			email="your@email.com"
		)

		follow(self.you, self.me)

	def test_create(self):
		action = create(self.me, self.you, "follows")
		self.assertIsNotNone(action)

	def test_get_newsfeed(self):
		action = create(self.me, self.you, "beats")
		newsfeed = get_newsfeed(self.you)
		self.assertIn(action, newsfeed)

	def test_get_activities(self):
		action = create(self.me, self.you, "steal")
		activities = get_activities(self.me)
		self.assertIn(action, activities)

