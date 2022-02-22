import pyautogui, time

#minimize all windows to make sure right click is happening on the desktop
pyautogui.keyDown('winleft')
pyautogui.press('d')
pyautogui.keyUp('winleft')

#get screen size and calculate mouse positions
w, h = pyautogui.size()
width = int(w) - 1
height = int(h) - 1
firstPositionX = round(width / 2)
firstPositionY = round(height / 2)
secondPositionX = round(width / 4)
secondPositionY = round(height / 4)

#move cursor and right click to avoid sleep or end script when cursor is moved to bottom-right corner
while True:
    x, y = pyautogui.position()

    if x != width and y != height:
        pyautogui.moveTo(firstPositionX, firstPositionY, 2)
        pyautogui.click(button='right')
        time.sleep(5)
    else:
        break
    
    x, y = pyautogui.position()

    if x != width and y != height:
        pyautogui.moveTo(secondPositionX, secondPositionY, 2)
        pyautogui.click(button='right')
        time.sleep(5)
    else:
        break
