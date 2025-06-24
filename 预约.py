import pyautogui
import pyperclip
import os
import time

x = 1422
y = 819
target_time = "23:59:59"

print("脚本启动，等待执行时间:", target_time)
start_script = time.time()  # 脚本开始计时

while True:
    time_now = time.strftime("%H:%M:%S", time.localtime())  # 当前时间

    if time_now == target_time:
        reach_time = time.time()
        print(f"达到目标时间：{time_now}")
        print(f"等待时间耗时：{reach_time - start_script:.2f} 秒")

        # 鼠标拖动
        t1 = time.time()
        pyautogui.dragTo(x, y)
        t2 = time.time()
        print(f"鼠标拖动耗时：{t2 - t1:.2f} 秒")
        # 拖动后延时 0.9 秒
        print("等待 0.9 秒后执行双击...")
        time.sleep(0.9)

        # 双击
        t3 = time.time()
        pyautogui.doubleClick()
        t4 = time.time()
        print(f"鼠标双击耗时：{t4 - t3:.2f} 秒")

        # 执行关机
        t5 = time.time()
        print("操作完成，准备关机...")
        os.system("shutdown /s /t 30")  # Windows：30 秒后关机
        t6 = time.time()
        print(f"执行关机命令耗时：{t6 - t5:.2f} 秒")

        break

    time.sleep(1)  # 每秒检查一次时间
