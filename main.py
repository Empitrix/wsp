#!/usr/bin/env python3
import argparse
from typing import Optional
from lib.database import get_path, Database
from lib.script.compiler import WSPCompiler
from lib.models import Script
from win32api import Sleep
import os, sys

from lib.utils import awpn

parser = argparse.ArgumentParser()

db:Database = Database(path=get_path())


parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", help="Saved Name", type=str)
parser.add_argument("-c", "--compile", help="Compile file [<FULL PATH>]", type=str)
parser.add_argument("-s", "--save", help="Save file [<FULL PATH>]", type=str)
parser.add_argument("-a", "--all", help="Show all the scripts", action="store_true", default=False)
parser.add_argument("-f", "--force", help="Force to replace script", action="store_true", default=False)
parser.add_argument("-d", "--delete", help="Delete script", type=str)
parser.add_argument("-l", "--listen", help="Listen to windows focus (for focus on wsps langauge)", action="store_true", default=False)

args = parser.parse_args()


if args.listen == True:
	print("Press <C-c> to quit\n")
	last:Optional[str] = ""
	try:
		while True:
			current = awpn()
			if current != last:
				print(current)
				last = current
			Sleep(200)
	except KeyboardInterrupt:
		print("Finished.")
		sys.exit()


if args.all == True:
	all:list[Script] = db.read_all()
	if len(all) == 0:
		print("There is no saved script\nUse '-s' to save for more info see '--help'")
	print("Name of all the saved scripts")
	for this in all:
		print(f">{this.name}<")


if args.save != None:
	if os.path.isfile(args.save):
		compiler:WSPCompiler = WSPCompiler()
		compiler.load_file(args.save)
		if compiler.script != None:
			compiler.try_parse()  # If everything is fine will pass the line
			# db.create(compiler.script)
			if(not db.access(compiler.script) and args.force):
				db.delete(compiler.script)
				db.create(compiler.script)
			else :
				db.create(compiler.script)

		else:
			print("Failed to save!")

	else:
		print("File is not exists or the path is incorrect")


if args.name != None:
	compiler:WSPCompiler = WSPCompiler()
	compiler.load_script(args.name)
	compiler.compile()


if args.compile != None:
	if os.path.isfile(args.compile):
		compiler:WSPCompiler = WSPCompiler()
		compiler.load_file(args.compile)
		compiler.compile()
	else:
		print("File is not exists or the path is incorrect")


if args.delete != None:
	compiler:WSPCompiler = WSPCompiler()
	compiler.load_script(args.delete)
	if compiler.script != None:
		db.delete(compiler.script)
		print(f"Delted: [{args.delete}]")
	else:
		print("Failed!\nScript not found")

