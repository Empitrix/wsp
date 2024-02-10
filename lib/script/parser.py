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


def split_by(pattren:str, data:str) -> list[str]:
	return re.split(pattren, data, flags=re.MULTILINE)


class WSPParser:
	def __init__(self, script:Script) -> None:
		self.script = script

	def parse(self) -> list[DebugLine]:
		"""Collect Valid Lines"""
		lines:list[DebugLine] = []

		# Apply Variables
		variables:list[str] = re.findall(r'^\!\@\s?\w+\s+=\s*\".*?\"\;', self.script.data, re.MULTILINE);

		for var in variables:
			captured_name = re.search(r'\!\@\s*\w+', var, re.MULTILINE)
			captured_value = re.search(r'\".*?\"', var, re.MULTILINE)
			if captured_name == None or captured_value == None:
				continue
			self.script.data = re.sub(r'\!\$' + re.sub(r'\!\@\s*', "", captured_name[0]), captured_value[0], self.script.data)
			self.script.data = self.script.data.replace(var, "")


		captured:list[str] = split_by(r'^\s*\/\/.*$', self.script.data)

		idx = 0
		for v1 in captured:
			for v2 in split_by(r';$', v1):
				if v2.strip() != "":
					if len(v2.lstrip().split('\n')) > 2:
						print(f"Inavalid syntax at: [{idx + 1}],\n\t>{v1}")
						sys.exit(0)
					dline = get_action(idx, f"{v2.strip()};")
					lines.append(dline)
					idx += 1
			idx += 1
		return lines




def get_action(idx:int, inpt:str) -> DebugLine:
	dline:Optional[DebugLine] = None
	for rule in get_rules():
		founded:list[str] = re.findall(rule.pattern, inpt, flags=re.MULTILINE);
		if len(founded) == rule.amount:
			debug_value:str = ""
			values = re.findall(r'\".*?\"', inpt, re.MULTILINE)
			if values == None:
				print(f"invalid line: [{idx}]\n\t>{inpt}")
				sys.exit()
			# Mix values them

			if len(values) == 0:
				print(f"Err: invalid parameter, line: [{idx}]\n\t>{inpt}")
				sys.exit()

			for v in values:
				debug_value += v[1:-1] 

			dline = DebugLine(idx=idx, line=inpt, action=rule.action, value=debug_value)
		elif len(founded) > rule.amount:
			print(f"ERR: in line: {idx}")
			sys.exit()
		else:
			continue

	if dline == None:
		print(f"ERR!, invalid syntax at: line [{idx + 1}]\n> {inpt}")
		sys.exit()

	return dline




