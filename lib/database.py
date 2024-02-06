import os, json
from .models import Script, parse_script
from typing import Optional


def get_path() -> str:
	"""Get the DB file path and if not exists create one."""
	# 'C:\Users\<User>\AppData\Local\Programs\WSP\db.json'
	path:str = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Programs', 'WSP')
	if not os.path.isdir(path):
		os.makedirs(path)
	db_path:str = os.path.join(path, 'db.json')
	if not os.path.exists(db_path):
		open(db_path, "x+").close()
		# Initialize
		Office(path=db_path).write({ 'scripts': [] })
	return db_path


def get_access(name:str, items:dict[str, list]) -> bool:
	for i in items['scripts']:
		if i['name'] == name:
			return False
	return True


class Office:
	def __init__(self, path:str) -> None:
		self.dbp = path
	
	def write(self, data:dict[str, list]) -> None:
		"""Write on the input .Json file"""
		with open(self.dbp, "w+") as jf:
			jf.write(json.dumps(data))

	def read(self) -> dict[str, list]:
		"""Read the input .Json file"""
		with open(self.dbp, "r+") as jf:
			return json.load(jf)


class Database:
	def __init__(self, path:str) -> None:
		"""Database OBJ that do the CRUD for scripts"""
		self.office = Office(path=path)


	def create(self, inpt:Script) -> bool:
		"""Create a new Script"""
		data:dict[str, list] = self.office.read()
		access = get_access(name=inpt.name, items=data)
		if access:
			data["scripts"].append(inpt.to_json())
			self.office.write(data)
		return access


	def read(self, name:str) -> Optional[Script]:
		"""Collect Singe Script data by name"""
		data:dict[str, list] = self.office.read()
		collect:dict[str, str] = {}
		for i in data["scripts"]:
			if i['name'] == name:
				collect = i
		if collect == {}:
			return None
		return parse_script(collect)


	def read_all(self) -> list[Script]:
		"""Get all the Scripts as list"""
		data:dict[str, list] = self.office.read()
		collect:list[Script] = []
		for i in data['scripts']:
			collect.append(parse_script(i))
		return collect


	def update(self, old:Script, script:Script) -> bool:
		"""Update selected script with the new one"""
		data:dict[str, list] = self.office.read()
		access = get_access(name=script.name, items=data)
		if access:
			for idx, itm in enumerate(data['scripts']):
				if itm['name'] == old.name:
					data['scripts'][idx] = script.to_json()
			self.office.write(data)
		return access


	def delete(self, inpt:Script) -> None:
		"""Delete given script"""
		data:dict[str, list] = self.office.read()
		itms:list = []
		for i in data['scripts']:
			if i['name'] != inpt.name:
				itms.append(i)
		data['scripts'] = itms
		self.office.write(data)

