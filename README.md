django-newsfeed
===============

TODO
A small django app for news feed inspired by django-activity-stream. It uses fan-out-on-load to build the user news feed on demand. There is a cache layer (Redis) that stores the most recent activities of a user (the number of the recent items to store is configurable in the settings) for faster news feed loading.
