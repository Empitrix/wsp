#!/usr/bin/env python3
from lib.database import get_path, Database
from lib.script.compiler import WSPCompiler
# from lib.models import Script
# import os

db:Database = Database(path=get_path())
compiler:WSPCompiler = WSPCompiler()


