from lib.models import Script
# import re

"""\
.wsps file
// This is just a comments

// Setup focus window (If not defined: work with any window)
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

class WSPParser:
	def __init__(self, script:Script) -> None:
		self.script = script

