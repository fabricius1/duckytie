from pygame import mixer
from gtts import gTTS
import time
import os


# PART 1
def read_text_aloud(text, filename="temp.mp3", delete_mp3=True, language="en", slow=False):
    # PART 2
    audio = gTTS(text, lang=language, slow=slow)
    audio.save(filename)

    # PART 3
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()

    # PART 4
    seconds = 0
    while mixer.music.get_busy() == 1:
        time.sleep(0.25)
        seconds += 0.25

    # PART 5
    mixer.quit()
    if delete_mp3:
        os.remove(filename)
    print(f"mp3 file played for {seconds} seconds")


if __name__ == "__main__":
    read_text_aloud(
        "This is the main module. This program has finished. Thanks for running it!")
