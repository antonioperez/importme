# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='date_start',
            field=models.DateTimeField(null=True),
        ),
    ]
