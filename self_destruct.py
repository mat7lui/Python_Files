import pyautogui, time


def destroy():
    pyautogui.click(1400, 300)
    time.sleep(1)
    pyautogui.hotkey("command", "down")
    pyautogui.typewrite("# VICTORY IS MINE!")
    pyautogui.hotkey("command", "a")
    pyautogui.hotkey("command", "/")


destroy()
