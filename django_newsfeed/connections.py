from django.contrib.contenttypes.models import ContentType

from .models import Follow

def follow(user, followed):
	"""
		User follows an object.
	"""

	follow, create = Follow.objects.get_or_create(
		user=user,
		object_id=followed,
		followed=ContentType.objects.get_for_model(followed)
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
		followed=ContentType.objects.get_for_model(followed)
	).delete()


def is_following(user, followed):
	"""
		Checks if the user is already following an object.
	"""

	return bool(Follow.objects.count(
		user=user,
		object_id=followed.pk,
		followed=ContentType.objects.get_for_model(followed)
	))


def followers(user):
	"""
		Returns a queryset of all the followers of a given
		user.
	"""

	return Follow.objects.filter(
		object_id=user.pk,
		followed=ContentType.objects.get_for_model(user)
	)


def following(user):
	"""
		Returns all the objects that `user` is following.
	"""

	return Follow.objects.filter(
		user=user
	)
