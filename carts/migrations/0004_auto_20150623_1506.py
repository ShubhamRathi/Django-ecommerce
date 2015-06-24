# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20150623_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
