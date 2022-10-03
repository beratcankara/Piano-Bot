import pyautogui
import keyboard
#pyautogui.displayMousePosition()
while keyboard.is_pressed("q") == False:
    if pyautogui.pixel(402,530)[0] == 0:
        pyautogui.click(402,530)
    elif pyautogui.pixel(549,530)[0] == 0:
        pyautogui.click(549,530)
    elif pyautogui.pixel(671,530)[0] == 0:
        pyautogui.click(671,530)
    elif pyautogui.pixel(790,530)[0] == 0:
        pyautogui.click(790,530)
# 1 = X:  567 Y:  530, 2 = X:  402 Y:  530, 3 = X:  549 Y:  530, 4 = X:  671 Y:  530