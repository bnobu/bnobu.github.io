from gtts import gTTS
import time
import os
import sys

def say(text):
    tts = gTTS(text)
    filename = "temp.mp3"
    tts.save(filename)
    if sys.platform.startswith("win"):
        os.system(f"start {filename}")
    else:
        os.system(f"mpg123 {filename} > /dev/null 2>&1")
    time.sleep(1)
    try:
        os.remove(filename)
    except:
        pass

# Get timer length
minutes = int(input("⏳ Enter timer length in minutes: "))
total_seconds = minutes * 60

say(f"Timer started for {minutes} minutes")
print(f"⏰ Timer started for {minutes} minutes...\n")

five_min_mark = 5 * 60
three_min_mark = 3 * 60

# Track if we've announced checkpoints
said_five = False
said_three = False

for remaining in range(total_seconds, -1, -1):
    mins, secs = divmod(remaining, 60)
    time_display = f"{mins:02d}:{secs:02d}"
    print(f"\r⏳ Time left: {time_display}", end="", flush=True)

    if remaining == five_min_mark and total_seconds > five_min_mark and not said_five:
        say("5 minutes remaining")
        said_five = True
    elif remaining == three_min_mark and total_seconds > three_min_mark and not said_three:
        say("3 minutes remaining")
        said_three = True

    time.sleep(1)

say("All done!")
print("\n✅ Timer finished.")
