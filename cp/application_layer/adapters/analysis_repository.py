import logging
from datetime import datetime

from sqlalchemy import or_

from cp.app import db

logger = logging.getLogger("flask.app."+__name__)

