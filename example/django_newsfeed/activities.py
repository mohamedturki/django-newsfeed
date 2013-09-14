from django.contrib.contenttypes.models import ContentType

from .models import Action
from .connections import following

def create(actor, target, verb):
    """
        Creates a new activity.
    """
    return Action.objects.create(
        actor_object_id=actor.pk,
        actor_content_type=ContentType.objects.get_for_model(actor),
        target_object_id=target.pk,
        target_content_type=ContentType.objects.get_for_model(target),
        verb=verb
    )


def get_newsfeed(user):
    """
        Returns the activities of all the objects
        that `user` is following.
    """
    return Action.objects.filter(
    	actor_object_id__in=[followed.pk for followed in following(user)]
    )


def get_activities(user):
    """
        Returns all the activities of a user.
    """
    return Action.objects.filter(
    	actor_object_id=user.pk
    )