from django.contrib.contenttypes.models import ContentType

from .models import Follow, Action

def follow(user, followed):
	"""
		User follows an object.
	"""

	follow, create = Follow.objects.get_or_create(
		user=user,
		object_id=followed,
		content_type=ContentType.objects.get_for_model(followed)
	)

def unfollow(user, followed):
	"""
		Unfollows an object.
		Removes all the connections between the user
		and the followed object.
	"""

	Follow.objects.filter(
		user=user,
		object_id=followed.pk,
		content_type=ContentType.objects.get_for_model(followed)
	)
