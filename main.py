#!/usr/bin/env python3
import os
from lib.database import get_path, Database
from lib.script.compiler import WSPCompiler
# from lib.models import Script
# import os

db:Database = Database(path=get_path())
compiler:WSPCompiler = WSPCompiler()

compiler.load_file(os.path.join(os.getcwd(), "test.wsps"))
compiler.compile()

