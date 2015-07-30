# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20150605_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(related_name='tags', to='blog.Post'),
        ),
    ]
