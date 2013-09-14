from datetime import datetime

from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType


from .settings import USER_MODEL

class Follow(models.Model):
	"""
	"""	
	user = models.ForeignKey(USER_MODEL)
	object_id = models.PositiveIntegerField()
	content_type = models.ForeignKey(ContentType)
	followed = generic.GenericForeignKey('content_type', 'object_id')
	date = models.DateTimeField(default=datetime.now())

	def __unicode__(self):
		return "{0} follows {1}".format(
			self.user.username,
			self.followed
		)


class Action(models.Model):
	"""
	Actions performed by objects.
	<actor> <verb> <target> <time>
	"""
	actor_object_id = models.PositiveIntegerField()
	actor_content_type= models.ForeignKey(
		ContentType,
		related_name='actor'
	)
	actor = generic.GenericForeignKey(
		'actor_content_type',
		'actor_object_id'
	)
	target_object_id = models.PositiveIntegerField()
	target_content_type= models.ForeignKey(
		ContentType,
		related_name='target'
	)
	target = generic.GenericForeignKey(
		'target_content_type',
		'target_object_id'
	)
	verb = models.CharField(max_length=200)
	date = models.DateTimeField(default=datetime.now())
	
	def __unicode__(self):
		return "{0} {1} {2} at {3}".format(
			self.actor,
			self.verb,
			self.target,
			self.date
		)