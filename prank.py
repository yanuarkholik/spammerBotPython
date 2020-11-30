import pyautogui, time

time.sleep(5)
f = open("nama_file_spam", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
