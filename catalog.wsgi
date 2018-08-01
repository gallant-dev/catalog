#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/catalog/")


from __init__ import app as application
application.secret_key = '<b\x1f\xa3\x01\xf0\xc9X\x06\xe00\xfb\xba\x15\x92\x92'
