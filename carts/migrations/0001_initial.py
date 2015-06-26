# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.DecimalField(default=0.0, max_digits=100, decimal_places=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line_total', models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)),
                ('notes', models.TextField(null=True, blank=True)),
                ('quantity', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('cart', models.ForeignKey(blank=True, to='carts.Cart', null=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
    ]
