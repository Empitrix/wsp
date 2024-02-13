import os, sys
from typing import Optional
from lib.database import Database, get_path
from lib.models import DebugAction, DebugLine, Script
from lib.script.parser import WSPParser
from lib.utils import DebugUtils
from win32api import Sleep


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

	def try_parse(self):
		"""Try to parse script"""
		if self.script != None:
			WSPParser(script=self.script).parse()
		else:
			print("Script is not found!")


	def load_script(self, name:str):
		"""Use pre-load saved is database scripts"""
		result:Optional[Script] = self.db.read(name=name)
		if result == None:
			print("Script not Exsit!\nUse '-a' flag to see all the saved scripts")
			sys.exit(127)
		self.script = result
		return result

	def compile(self) -> None:
		"""Compile the scriopt"""
		if self.script == None:
			print("Invalid Data! (script is not found)")
			sys.exit()
		lines:list[DebugLine] = WSPParser(script=self.script).parse()

		current_focus:str = ""
		utils:DebugUtils = DebugUtils()
		for line in lines:
			if line.action == DebugAction.FOCUS:
				current_focus = line.value.strip()

			# Wait until right focus
			utils.wait_for_foucs(current_focus)

			# Main Actions
			match line.action:
				case DebugAction.PRINT:
					print(line.value)
				case DebugAction.DELAY:
					Sleep(int(line.value))
				case DebugAction.SHORT:
					utils.press_hot_key(line.value)
				case DebugAction.TYPING:
					utils.type_word(line.value)


