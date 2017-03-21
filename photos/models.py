# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative commons')
)

PUBLIC = 'PUB'
PRIVATE = 'PRI'

VISIBILITY = (
    (PUBLIC, 'Public'),
    (PRIVATE, 'Private')
)

class Photo(models.Model):

    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, null=True, default="")
    creation_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)

    def __unicode__(self):
        return self.name
