import os, sys
from typing import Optional
from lib.database import Database, get_path
from lib.models import DebugLine, Script
from lib.script.parser import WSPParser


class WSPCompiler:
	def __init__(self) -> None:
		"""This is for converting *.wsps to valid python code"""
		self.db:Database = Database(path=get_path())
		self.script:Optional[Script] = None 


	def load_file(self, path:str) -> Script:
		"""Load the script using path"""
		if not os.path.exists(path):
			print('File is not Exsit!')
			sys.exit(127)
		script:Script = Script(name="", data="")
		with open(path, 'r') as sf:
			# Get file name as name for script
			script.name = os.path.splitext(os.path.basename(path))[0]
			script.data = sf.read()
		if script.name == "":
			print("Invalid data!")
			sys.exit()
		self.script = script
		return script


	def load_script(self, name:str):
		"""Use pre-load saved is database scripts"""
		result:Optional[Script] = self.db.read(name=name)
		if result == None:
			print('Script not Exsit!')
			sys.exit(127)
		self.script = result
		return result

	def compile(self) -> None:
		"""Compile the scriopt"""
		if self.script == None:
			print("Invalid Data! (script is not found)")
			sys.exit()
		lines:list[DebugLine] = WSPParser(script=self.script).parse()
		for line in lines:
			# print(line.line, "->", line.value, "-->", line.action)
			print(line.line)


