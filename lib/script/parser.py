from lib.models import DebugLine, Script
from typing import Optional
import re, sys

from lib.script.rules import get_rules
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
				if v2.strip() != "":
					# dline = DebugLine(idx=idx, line=v2.strip())
					dline = get_action(idx, f"{v2.strip()};")
					# get_action(idx, dline.line)
					lines.append(dline)
					idx += 1
			idx += 1
		return lines




def get_action(idx:int, inpt:str) -> DebugLine:
	dline:Optional[DebugLine] = None
	for rule in get_rules():
		# founded:list[str] = re.findall(rule.pattern, inpt);
		founded:list[str] = re.findall(rule.pattern, inpt, flags=re.MULTILINE);
		if len(founded) == rule.amount:
			dline = DebugLine(idx=idx, line=inpt, action=rule.action, value="")
		elif len(founded) > rule.amount:
			print(f"ERR: in line: {idx}")
			sys.exit()
		else:
			# print("This is Less, This action did not matched!")
			continue

	if dline == None:
		print(f"ERR!, invalid syntax at: line [{idx + 1}]\n> {inpt}")
		sys.exit()
	print(dline.line)
	return dline

