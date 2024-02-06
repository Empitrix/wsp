#!/usr/bin/env python3
from lib.database import get_path, Database
from lib.models import Script

db:Database = Database(path=get_path())
# office:Office = Office(path=get_path())
# office.write({ 'scripts': [] })

scriptA:Script = Script(name="Test-A", data="A")
scriptB:Script = Script(name="Test-B", data="B")
scriptC:Script = Script(name="Test-C", data="C")
scriptD:Script = Script(name="Test-D", data="D")


# print(db.create(inpt=scriptA))
print(db.update(old=scriptA, script=scriptB))
