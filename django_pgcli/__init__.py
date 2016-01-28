# -*- coding: utf-8 -*-

__author__ = 'Ash Christopher'
__email__ = 'ash.christopher@gmail.com'
__version__ = '0.0.2'
__maintainer__ = 'Nikolay Bryskin'


from django.db.backends.postgresql_psycopg2.client import DatabaseClient

DatabaseClient.executable_name = 'pgcli'
