from lib.models import DebugAction, Rule


def get_rules() -> list[Rule]:
	"""Valid regex rules per amount(line)
	Initialized in function for memory usage"""
	return [
		# Rule(pattern=r'#!focus:', amount=1, action=DebugAction.FOCUS),
		Rule(r'#!focus:', 1, DebugAction.FOCUS),
		Rule(r'#!delay:', 1, DebugAction.DELAY),
		Rule(r'#!short:', 1, DebugAction.DELAY),

		# Funcs
		Rule(r'!print', 1, DebugAction.DELAY),

		# Variables
	]
