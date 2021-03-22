from pygame import mixer
from gtts import gTTS
import time
import os

if os.name == "posix":
    from pydub import AudioSegment


# PART 1
def say(text, filename="temp.mp3", delete_audio_file=True, language="en", slow=False):
    # PART 2
    audio = gTTS(text, lang=language, slow=slow)
    audio.save(filename)

    if os.name == "posix":
        sound = AudioSegment.from_mp3(filename)
        old_filename = filename
        filename = filename.split(".")[0] + ".ogg"
        sound.export(filename, format="ogg")
        if delete_audio_file:
            os.remove(old_filename)

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
    if delete_audio_file:
        os.remove(filename)
    print(f"audio file played for {seconds} seconds")


if __name__ == "__main__":
    say("You are worthy of love!")
    time.sleep(1.5)
    say("This is the main module. This program has finished. Thanks for running it!")
