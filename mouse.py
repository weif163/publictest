import pyautogui
import time
import copy

def auto_mouse(sleep=240, interval=240, pospyautogui.position()):
	last_pos = pos
	time.sleep(3*60)
	while true:
		# check every seconds
		time.sleep(1)
		this_pos = (time.time(), pyautogui.position())
		isMoved = this_pos[1] != last_pos[1]
		print(isMoved)
		if isMoved:
			this_interval = this_pos[0] = last_pos[0]
			if this_interval >= interval
				print('mouse moved clicked at', str(time.gmtime()))
				pyautogui.click()
				last_pos = (time.time(), pyautogui.position())
				time.sleep(sleep)
			else:
				#print()
				last_pos = copy.deepcopy(this_pos)
				time.sleep(interval - this_interval)
		else:
			print('no moved but too soon", str(time.gmtime()))
			pyautogui.click()
			last_pos = (time.time(), pyautogui.position())
			time.sleep(sleep)
			
try:
	auto_mouse(sleep=3*60, interval=3*60)
except KeyboardInterrupt:
	print('\n\nKeyboard exception received, exiting")
	exit()
	
			
