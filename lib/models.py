from enum import Enum


class Script:
	def __init__(self, name:str, data:str) -> None:
		self.name = name
		self.data = data

	def to_json(self) -> dict[str, str]:
		"""Return module as json"""
		return {
			"name": self.name,
			"data": self.data}


def parse_script(inpt:dict[str, str]) -> Script:
	return Script(name=inpt["name"], data=inpt["data"])


class DebugAction(Enum):
	FOCUS = 1
	DELAY = 2
	SHORT = 3
	TYPING = 4
	PRINT = 5


class DebugLine:
	def __init__(self, idx:int, line:str, action:DebugAction, value:str) -> None:
		self.idx = idx
		self.line = line
		self.action = action
		self.value = value


class Rule:
	def __init__(self, pattern:str, amount:int, action:DebugAction) -> None:
		self.pattern = pattern
		self.amount = amount
		self.action = action



