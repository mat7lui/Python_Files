# countdown.py - A simple countdown script

import time, subprocess

timeLeft = 10
print(f"Count begun, in T minus {timeLeft}")
time.sleep(1)
timeLeft -= 1

while timeLeft > 0:
    print(timeLeft, end="..")
    time.sleep(1)
    timeLeft -= 1

# TODO: at the end of the countdown, play the sound
subprocess.Popen(["open", "/System/Library/Sounds/Hero.aiff"])
