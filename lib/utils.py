import win32com.client as comclt
import pyautogui
from win32api import Sleep
import win32gui, win32process, psutil
from typing import Optional


class DebugUtils:
	def __init__(self) -> None:
		pass

	@staticmethod
	def type_word(word:str, enter:bool = False) -> None:
		"""Type Phrase"""
		wsh = comclt.Dispatch("WScript.Shell")
		wsh.SendKeys(word)
		if enter :
			wsh.SendKeys("{ENTER}")


	@staticmethod
	def press_hot_key(keys:str) -> None:
		"""Press Shortcut"""
		pyautogui.hotkey(*[key.strip() for key in keys.split("+")])
		Sleep(500)	# wait for action


	@staticmethod
	def wait_for_foucs(name:str):
		"""Sleep until right foucs window"""
		# Close function if there is no focus
		name = name.strip()
		if name == "":
			return
		# Wait until name
		while True:
			if awpn() == name:
				break;
			Sleep(800)  # 0.8s




def awpn() -> Optional[str]:
	"""Active window process name"""
	try:
		pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
		return psutil.Process(pid[-1]).name()
	except:
		pass




