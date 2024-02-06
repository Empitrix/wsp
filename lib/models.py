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
