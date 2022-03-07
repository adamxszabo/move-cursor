import pyautogui, keyboard

#minimize all windows to make sure right click is happening on the desktop
pyautogui.keyDown('winleft')
pyautogui.press('d')
pyautogui.keyUp('winleft')

#get screen size and calculate mouse positions
w, h = pyautogui.size()
width, height = int(w), int(h)
firstPosition = (round(width / 2), round(height / 2))
secondPosition = (round(width / 4), round(height / 4))

#function to terminate script when escape is pressed
def failSafe():
    if keyboard.is_pressed('escape'):
        print('Script terminated by user pressing escape')
        return True

#move cursor and right-click to avoid sleep or end script escape is pressed
while True:
        pyautogui.moveTo(firstPosition[0], firstPosition[1], 1)
        if failSafe():
            break
        pyautogui.click(button='right')        
        if failSafe():
            break
        pyautogui.moveTo(secondPosition[0], secondPosition[1], 1)
        if failSafe():
            break
        pyautogui.click(button='right')
        if failSafe():
            break
