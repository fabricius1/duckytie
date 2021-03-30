from pygame import mixer
from gtts import gTTS
import time
import os

if os.name == "posix":
    from pydub import AudioSegment


def _check_filename(filename):
    if not filename.endswith(".mp3") and not filename.endswith(".ogg"):
        raise ValueError('filename parameter value must end with ".mp3" or ".ogg", '
                         'depending on your OS system.')

    if filename.endswith(".mp3") and os.name == "posix":
        raise OSError('Since os.name == "posix", the filename parameter value '
                      'must end with ".ogg".')

    if filename.endswith(".ogg") and os.name != "posix":
        raise OSError('Since os.name != "posix", the filename parameter value '
                      'must end with ".mp3".')


def _delete_audio(audio_filename, must_delete=True):
    _check_filename(audio_filename)
    if must_delete:
        os.remove(audio_filename)
    return must_delete


def create_audio(text, filename="temp", language="en", slow=False):
    if "." in filename:
        raise ValueError("The filename parameter value can't have the dot "
                         "character (.) or any file extension")

    filename += ".mp3"

    audio = gTTS(text, lang=language, slow=slow)
    audio.save(filename)

    if os.name == "posix":
        sound = AudioSegment.from_mp3(filename)
        old_filename = filename
        filename = filename.split(".")[0] + ".ogg"
        sound.export(filename, format="ogg")
        os.remove(old_filename)

    return filename


def play_audio(audio_filename, must_delete=True):
    _check_filename(audio_filename)
    mixer.init()
    mixer.music.load(audio_filename)
    mixer.music.play()

    seconds = 0
    while mixer.music.get_busy() == 1:
        time.sleep(0.25)
        seconds += 0.25

    mixer.quit()
    _delete_audio(audio_filename, must_delete)


def say(text, audio_filename="temp", language="en",
        slow=False, must_delete=True):

    audio_filename = create_audio(text, audio_filename, language, slow)
    play_audio(audio_filename, must_delete)


if __name__ == "__main__":
    say("You are worthy of love!")
    time.sleep(1.5)
    say("This is the main module. This program has finished. Thanks for running it!")


# def say(text, filename="temp.mp3", delete_audio_file=True, language="en", slow=False):
#     audio = gTTS(text, lang=language, slow=slow)
#     audio.save(filename)

#     if os.name == "posix":
#         sound = AudioSegment.from_mp3(filename)
#         old_filename = filename
#         filename = filename.split(".")[0] + ".ogg"
#         sound.export(filename, format="ogg")
#         if delete_audio_file:
#             os.remove(old_filename)

#     mixer.init()
#     mixer.music.load(filename)
#     mixer.music.play()

#     seconds = 0
#     while mixer.music.get_busy() == 1:
#         time.sleep(0.25)
#         seconds += 0.25

#     mixer.quit()
#     if delete_audio_file:
#         os.remove(filename)
#     print(f"audio file played for {seconds} seconds")
