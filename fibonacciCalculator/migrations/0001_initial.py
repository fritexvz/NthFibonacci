# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FibonacciNumbers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField()),
                ('value', models.IntegerField()),
                ('time', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('method', models.CharField(max_length=50)),
            ],
        ),
    ]
