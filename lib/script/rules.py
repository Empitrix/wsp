from lib.models import DebugAction, Rule


def get_rules() -> list[Rule]:
	"""Valid regex rules per amount(line)
	Initialized in function for memory usage"""
	return [
		# Rule(r'#!focus:', 1, DebugAction.FOCUS),
		Rule(r'#!focus:\s*\".*?\"\;', 1, DebugAction.FOCUS),
		Rule(r'#!delay:\s*[0-9]*;', 1, DebugAction.DELAY),
		Rule(r'#!short:\s*\".*?\"\;', 1, DebugAction.SHORT),
		Rule(r'##!type:\s*\".*?\"\;', 1, DebugAction.TYPING),
		# Funcs
		Rule(r'\!print\(.*?\)\;', 1, DebugAction.FUNCTION),
	]
