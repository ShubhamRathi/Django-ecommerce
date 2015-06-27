# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_variations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(default=b'ABC', unique=True, max_length=120)),
                ('status', models.CharField(default=b'Started', max_length=120, choices=[(b'Started', b'Started'), (b'Abandoned', b'Abandoned'), (b'Finished', b'Finished')])),
                ('sub_total', models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)),
                ('tax_total', models.DecimalField(default=0.0, max_digits=1000, decimal_places=2)),
                ('final_total', models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(to='carts.Cart')),
            ],
        ),
    ]
