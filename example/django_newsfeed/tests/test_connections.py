from django.test import TestCase
from django.contrib.auth.models import User

from ..connections import follow, unfollow, is_following, followers, following
from ..models import Follow

class ConnectionsTest(TestCase):

	def setUp(self):
		self.me = User.objects.create_user(
			username="mohamed",
			email="turkipro@gmail"
		)

		self.you = User.objects.create_user(
			username="yourusername",
			email="your@email.com"
		)

	def test_follow(self):
		follow(self.me, self.you)
		self.assertTrue(
			Follow.objects.filter(
				user=self.me, object_id=self.you.pk
			).count() > 0
		)

	def test_unfollow(self):
		unfollow(self.me, self.you)
		self.assertEqual(
			Follow.objects.filter(user=self.me, object_id=self.you.pk).count(), 0
		)

	def test_is_following(self):
		follow(self.me, self.you)
		self.assertTrue(is_following(self.me, self.you))

	def test_followers(self):
		follow(self.me, self.you)
		self.assertIn(self.me, followers(self.you))

	def test_following(self):
		follow(self.me, self.you)
		self.assertIn(self.you, following(self.me))