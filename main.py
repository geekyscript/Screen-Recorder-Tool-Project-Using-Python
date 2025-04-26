import cv2
import numpy as np
import pyautogui
import time

output_file = 'recording1.avi'
fps = 20.0
duration = 100  # seconds

screen_size = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_file, fourcc, fps, screen_size)

print("Recording started...")
start_time = time.time()

while time.time() - start_time < duration:
    frame = np.array(pyautogui.screenshot())
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame)

out.release()
print(f"Recording saved as {output_file}")
