from lib.models import DebugLine, Script
import re
# import re

"""\
.wsps file
// This is just a comments

// Setup focus window (If not defined <nill>: work with any window)
#!focus: "<FOCUS WINDOW>";

// Setup shortcut string
#!short: "<SHORTCUT>";

// Phrase that need to be typed
#!type: "<Word / Sentence / etc..>";

// Set delay time
#!delay: <Delay as millisecond (int)>;

// Variables Deinfe
// #@ <Name> = "<VALUE>";
// Usage
// #$<Name>;

// Pritn meethod for printing
!print("<DATA>");
"""

# def is_junk_line(inpt:str) -> bool:
# 	status:bool = False
# 	if inpt.strip() == "":
# 		status = True
# 	return status


class WSPParser:
	def __init__(self, script:Script) -> None:
		self.script = script

	def parse(self) -> list[DebugLine]:
		"""Collect Valid Lines"""
		lines:list[DebugLine] = []
		captured:list[str] = re.split(r'^\s*\/\/.*$', self.script.data, flags=re.MULTILINE)
		idx = 0
		for v1 in captured:
			for v2 in v1.split(';'):
				lines.append(DebugLine(idx=idx, line=v2.strip()))
				idx += 1
			idx += 1
		return lines


