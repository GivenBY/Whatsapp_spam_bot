import pyautogui
import time

pyautogui.FAILSAFE = True

try:
    k = int(input("Enter Number of times to repeat: "))
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
    exit()

msg = input("Enter a Msg You Want to Repeat: ")

i = 0
time.sleep(5)
while i < k:
    pyautogui.write(msg)
    pyautogui.press("enter")
    i += 1
