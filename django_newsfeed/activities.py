from django.contrib.contenttypes.models import ContentType

from .models import Action
from .connections import following

def create(actor, target, verb):
    """
        Creates a new activity.
    """
    return Action.objects.create(
        actor_object_id=actor.pk,
        actor=ContentType.objects.get_for_model(actor),
        target_object_id=target.pk,
        target=ContentType.objects.get_for_model(target),
        verb=verb
    )


def get_newsfeed(user):
    """
        Returns the activities of all the objects
        that `user` is following.
    """
    Action.objects.filter(
    	actor__in=following(user)
    )
    return True


def get_activities(user):
    """
        Returns all the activities of a user.
    """
    return True