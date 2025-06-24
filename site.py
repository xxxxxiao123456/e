import pyautogui
import time

print("请将鼠标移动到目标位置（3 秒内）...")
time.sleep(3)

x, y = pyautogui.position()
print(f"3 秒后鼠标位置：({x}, {y})")
