# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos Ventures SL

from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('custom_attributes', '0015_auto_20200615_0811'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userstorycustomattribute',
            unique_together=set([('project', 'name', 'type')]),
        ),
        migrations.AlterUniqueTogether(
            name='taskcustomattribute',
            unique_together=set([('project', 'name', 'type')]),
        ),
        migrations.AlterUniqueTogether(
            name='issuecustomattribute',
            unique_together=set([('project', 'name', 'type')]),
        ),
        migrations.AlterUniqueTogether(
            name='epiccustomattribute',
            unique_together=set([('project', 'name', 'type')]),
        ),
    ]
