#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/stud/tda072/public_html/flask_app/")
sys.path.insert(1,"/stud/tda072/public_html/flask_app/flask_app/")

from __init__ import app as application