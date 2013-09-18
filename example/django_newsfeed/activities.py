import json
from datetime import datetime

from django.contrib.contenttypes.models import ContentType
import redis as redispy

from .models import Action
from .connections import following

redis = redispy.StrictRedis(host='localhost', port=6379, db=0)


def create(actor, target, verb, meta):
    """
        Creates a new activity.
        TO REDIS:
        redis.set('user.{0}.activities', [items])
    """
    activity = {
        "actor": actor,
        "object": target,
        "action": verb,
        "meta": meta,
        "timestamp": str(datetime.now())
    }

    redis.rpush(
        'user.{0}.activities'.format(actor.get('id')),
        json.dumps(activity)
    )

    # return Action.objects.create(
    #     actor_object_id=actor.pk,
    #     actor_content_type=ContentType.objects.get_for_model(actor),
    #     target_object_id=target.pk,
    #     target_content_type=ContentType.objects.get_for_model(target),
    #     verb=verb
    # )


def get_activities(user_id):
    """
        Returns all the activities of a user in a json dumps.
        TO REDIS:
        activities = redis.get('user.{0}.activities')
    """
    return redis.lrange("user.{0}.activities".format(user_id), 0, -1)
    # return Action.objects.filter(
    #     actor_object_id=user.pk
    # )


def get_newsfeed(user):
    """
        Returns the activities of all the objects
        that `user` is following.
        TO REDIS:
        followeds = following(user)
        feed = []
        for followed in followed:
            feed.append(redis.get('user.{0}.activities'))
        sort_feed_somehow(feed)

    """
    return Action.objects.filter(
    	actor_object_id__in=[followed.pk for followed in following(user)]
    )
