# 🎥 How to Build Your Own Screen Recorder in Python (Command Line + GUI Version)

> **Capture your screen effortlessly** — Whether you're a developer, gamer, or content creator, this tutorial will teach you how to create a simple yet powerful **screen recording tool** in Python! 🚀

In this guide, we'll show you **two ways** to build your own **Python Screen Recorder**:
- A **command-line version** (super simple & lightweight 🎯)
- A **GUI version** (beautiful interface with countdown ⏳)

No prior experience? No problem!  
By the end, you'll have your own **custom screen recording app** ready to use.

---

## 📦 Prerequisites

Before diving in, install these Python packages:

```bash
pip install opencv-python pyautogui numpy
```

For the GUI version:

```bash
pip install tkinter
```
*(Tkinter usually comes built-in with Python, but install separately if missing.)*

---

## 1⃣ Create a Basic Command Line Screen Recorder in Python

Let's start with a **barebones but powerful** command-line screen recorder.

### Full Code:
```python
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
```

---

### 📋 How It Works:
- **Capture Screenshots** every frame using `pyautogui`.
- **Convert** screenshots to the correct color format for OpenCV.
- **Save** them as frames into a `.avi` video file.
- **Record duration** is based on a simple timer.

### 🧠 Pro Tips:
- Change `duration` to set how long the screen recording lasts.
- Adjust `fps` for smoother (or smaller size) videos.

---

## 2⃣ Build a Professional GUI Screen Recorder with Countdown ⏳

Now, let's **level up** and create a **Graphical User Interface (GUI)** for our screen recorder!  
This one looks and feels **slick and professional**!

### Full Code:
```python
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
    root.title("🔤 Screen Recorder")
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
```

---

## ✨ Why Build Your Own Screen Recorder in Python?

- **100% Customizable** — add webcam, add annotations, make it YOURS!
- **Lightweight** — No bloatware, only the features you want.
- **Learning Experience** — Understand real-world coding applications.
- **Fun Project** — Impress friends, employers, or clients!

---

## 📊 SEO Keywords Targeted
- Python screen recorder tutorial
- Build screen recorder Python
- Simple Python screen recorder
- Create GUI screen recording app
- Python screen capture script
- Record computer screen Python
- Best way to record desktop using Python
- OpenCV screen recording project

---

## 🚀 Conclusion

And there you have it — a full-fledged **Python Screen Recorder**, with both a quick **command-line version** and a gorgeous **GUI version**!

🔊 Whether you want to **capture gameplays**, **create tutorials**, or **record meetings**, this Python tool has you covered.

If you enjoyed this guide, make sure to **share** it with friends and **bookmark** for future reference! 🌟

Ready to take it even further?  
**Coming soon**: Add webcam capture, record system audio, schedule recordings automatically — stay tuned! 🎥✨

