#!/usr/bin/env python3
from lib.database import get_path, Database
# from lib.models import Script

db:Database = Database(path=get_path())

