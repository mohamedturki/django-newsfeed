from django.contrib.contenttypes.models import ContentType

from .models import Follow

def follow(user, followed):
	"""
		User follows an object.
	"""
	follow, create = Follow.objects.get_or_create(
		user=user,
		object_id=followed.pk,
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
	).delete()


def is_following(user, followed):
	"""
		Checks if the user is already following an object.
	"""

	return bool(Follow.objects.filter(
		user=user,
		object_id=followed.pk,
		content_type=ContentType.objects.get_for_model(followed)
	).count())


def followers(user):
	"""
		Returns a list of all the followers of a given
		user.
	"""
	follows = Follow.objects.filter(
		object_id=user.pk,
		content_type=ContentType.objects.get_for_model(user)
	)
	return [follow.user for follow in follows]


def following(user):
	"""
		Returns all the objects that `user` is following.
	"""
	follows = Follow.objects.filter(user=user)
	return [follow.followed for follow in follows]
