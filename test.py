#!/usr/bin/env python3
import os
from lib.database import get_path, Database
from lib.models import Script
from lib.script.compiler import WSPCompiler

db:Database = Database(path=get_path())
# office:Office = Office(path=get_path())
# office.write({ 'scripts': [] })

scriptA:Script = Script(name="Test-A", data="A")
scriptB:Script = Script(name="Test-B", data="B")
scriptC:Script = Script(name="Test-C", data="C")
scriptD:Script = Script(name="Test-D", data="D")


# print(db.create(inpt=scriptA))
print(db.update(old=scriptA, script=scriptB))


# LOADING
compiler:WSPCompiler = WSPCompiler()
# a = compilter.load_file(path=get_path())
a = compiler.load_file(path=os.path.join(os.getcwd(), "main.py"))
print(compiler.load_file(path=os.path.join(os.getcwd(), "main.py")).data)
