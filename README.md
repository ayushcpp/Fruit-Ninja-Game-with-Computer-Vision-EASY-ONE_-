# Fruit Ninja with Hand Tracking

Play Fruit Ninja with your index finger instead of a mouse.

![Python](https://img.shields.io/badge/python-3.8--3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

The script reads your webcam, tracks your hand with MediaPipe (via cvzone), and moves the system mouse to follow your index fingertip. Raise only your index finger to press the mouse button and slice; lower it or open your hand to let go.

> **Note:** This repo is the controller, not the game. You need a Fruit Ninja game (or any slicing game played with the mouse) running on your computer.

## Requirements

- Python 3.8 – 3.11 (the pinned `mediapipe` and `numpy` versions don't support newer Python)
- A webcam
- A Fruit Ninja game installed on your PC, or a browser version

## Installation

```bash
git clone https://github.com/ayushcpp/Fruit-Ninja-Game-with-Computer-Vision-EASY-ONE_-.git
cd Fruit-Ninja-Game-with-Computer-Vision-EASY-ONE_-

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
```

## How to Play

1. **Start the game.** Open Fruit Ninja and leave it on screen.
2. **Run the controller:**
   ```bash
   python fruit_ninja.py
   ```
3. A webcam preview window opens. Keep your hand inside the **purple box**. That box maps to your whole screen.
4. Switch to the game window and slice with your finger.

## Controls

| Gesture | Action |
| --- | --- |
| Move index finger | Move cursor |
| Only index finger up | Hold click (slice) |
| Any other hand pose | Release click |
| `q` (in the preview window) | Quit |

## Notes

- Built for Windows. On Linux, the `mouse` library needs root (`sudo`).
- Good lighting and a plain background make tracking more reliable.
- To change the gesture, edit the `only_index_up` check in `fruit_ninja.py`.

## License

[MIT](LICENSE)
