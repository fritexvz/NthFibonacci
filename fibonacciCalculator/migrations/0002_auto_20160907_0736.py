# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fibonacciCalculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonaccinumbers',
            name='time',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
    ]
