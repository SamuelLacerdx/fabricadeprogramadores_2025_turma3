import mouseinfo, pyautogui, time

pyautogui.press('super') 
pyautogui.write("navegador opera gx")
pyautogui.press('enter') 
pyautogui.click(314,56, duration=1)
time.sleep(1)
pyautogui.write("Sao Paulo fc")
pyautogui.press('enter') 
pyautogui.moveTo(428,241, duration=1)
pyautogui.click()
mouseinfo.mouseInfo()
