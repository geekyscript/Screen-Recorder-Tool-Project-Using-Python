import cv2
import numpy as np
import pyautogui
import time
import threading
import tkinter as tk
from tkinter import ttk

class ScreenRecorder:
    def __init__(self):
        self.recording = False
        self.out = None
        self.fps = 20.0
        self.output_file = 'recording.avi'

    def start_recording(self):
        screen_size = pyautogui.size()
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        self.out = cv2.VideoWriter(self.output_file, fourcc, self.fps, screen_size)

        self.recording = True
        threading.Thread(target=self.record).start()

    def stop_recording(self):
        self.recording = False

    def record(self):
        for i in range(3, 0, -1):
            countdown_var.set(f"Recording starts in {i}...")
            time.sleep(1)
        countdown_var.set("Recording in progress...")

        while self.recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            self.out.write(frame)

            if cv2.waitKey(1) == ord('q'):
                break

        self.out.release()
        cv2.destroyAllWindows()
        countdown_var.set("Recording saved as recording.avi")


def start():
    countdown_var.set("")
    recorder.start_recording()

def stop():
    recorder.stop_recording()


if __name__ == "__main__":
    recorder = ScreenRecorder()

    root = tk.Tk()
    root.title("🖥️ Screen Recorder")
    root.geometry("400x300")
    root.configure(bg="#1e1e1e")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton",
                    font=("Segoe UI", 12),
                    padding=10,
                    background="#3c3f41",
                    foreground="white")
    style.map("TButton",
              background=[("active", "#5c5f61")])

    title_label = tk.Label(root, text="Screen Recorder", font=("Segoe UI", 20, "bold"), fg="white", bg="#1e1e1e")
    title_label.pack(pady=20)

    start_button = ttk.Button(root, text="▶️ Start Recording", command=start)
    start_button.pack(pady=10)

    stop_button = ttk.Button(root, text="⏹️ Stop Recording", command=stop)
    stop_button.pack(pady=10)

    countdown_var = tk.StringVar()
    countdown_label = tk.Label(root, textvariable=countdown_var, font=("Segoe UI", 12), fg="lime", bg="#1e1e1e")
    countdown_label.pack(pady=10)

    root.mainloop()
