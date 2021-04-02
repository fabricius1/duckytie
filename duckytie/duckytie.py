"""The duckytie module makes it easy to write code that reads text aloud.

The following functions are available:
- say
- create_audio
- play_audio
- main

The say() function is the one you will probably use most. Actually, say() may be
the only one you will ever need to import from the duckytie module, by writing 
the following statement:

    from duckytie import say

You can read more about our functions in the respective docstrings.

This module also exports two more functions (_check_filename and _delete_audio) 
but their direct use in third-party programs is not recommended. They should be 
accessed only privately by code from this module. However, calling help() on 
them will show their docstring, which might be useful in some debugging 
scenarios.
"""

# '
import os
# The next line hides the pygame kind of annoying import printing.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
from typing import Union, List
from pygame import mixer
from gtts import gTTS
import time
import sys

if os.name == "posix":
    from pydub import AudioSegment


def _check_filename(filename: str) -> None:
    """ Check if the filename parameter follows these constraints:
        - 1) filename string must end with either ".mp3" or ".ogg";
        - 2) if os.name == "posix" evaluates to True, you can't have a filename ending in ".mp3";
        - 3) if os.name != "posix" evaluates to True, you can't have a filename ending in ".ogg".

        The three rules mentioned above exist so that computers whose operating system (OS) 
    is Linux or macOS will use only .ogg files in the play_audio() and _delete_audio()
    functions, while machines with Windows will use .mp3 files instead.

        Also, the underscore at the beginning of _check_filename intends to show that this function
    should not be used by itself but only privately, inside play_audio() and _delete_audio().

        Return None if no exception is raised. 
        Raise an error if any conditional statement becomes True. 
    """
    if not filename.endswith(".mp3") and not filename.endswith(".ogg"):
        raise ValueError('filename parameter value must end with ".mp3" or ".ogg", '
                         'depending on your OS system.')

    if filename.endswith(".mp3") and os.name == "posix":
        raise OSError('Since os.name == "posix" is True, the filename parameter value '
                      'must end with ".ogg".')

    if filename.endswith(".ogg") and os.name != "posix":
        raise OSError('Since os.name != "posix" is True, the filename parameter value '
                      'must end with ".mp3".')


def _delete_audio(audio_filename: str, must_delete: bool = True) -> None:
    """ Delete an audio file whose name is equal to the audio_filename parameter but only if
    must_delete is set to True.

        _check_filename(audio_filename) is called first inside _delete_audio().

        Also, the underscore at the beginning of _delete_audio intends to show that this function
    should not be used by itself but only privately, inside play_audio().

        Return None.
    """
    _check_filename(audio_filename)
    if must_delete:
        os.remove(audio_filename)


def create_audio(text: str, *, filename: str = "temp", language: str = "en", slow: bool = False) -> str:
    """ Create an audio file whose extension is either .mp3 or .ogg, depending on the
    operating system. 

        FUNCTION PARAMETERS:

        - text: string to be converted into an audio file; raise a TypeError if argument is not a string;
        - filename(default: "temp"): string with the audio filename. IMPORTANT: no dot 
    character should appear in the filename value. Otherwise, a ValueError will be raised 
    by the first conditional inside the function body;
        - language(default: "en"): string with the acronym of the language to be used to convert
    the text parameter to audio; if the language parameter value is not in the language_codes list,
    raise a ValueError;
        - slow(default: False): a boolean. If True, the created audio will be pronounced more slowly.

        "text" is the only positional parameter. All the others ones must be passed to the function
    as keyword arguments.

        FUNCTION LOGIC:

        After checking filename and language, a new filename string will be created with ".mp3" at 
    its end, since this is the audio format returned by the gTTS object initialization. Then, the mp3
    file will be saved in the local machine.
        However, if os.name == "posix", the mp3 file will be used to create a new ogg file with identical
    content before the mp3 file is deleted so that only one audio file will be saved in the machine (mp3
    if OS is Windows, ogg file otherwise).

        FUNCTION RETURN:

        Return the filename variable value, with the file extension (.ogg or .mp3). This string will be 
        used as the audio_filename argument, in the play_audio() function. 
    """
    language_codes = ["af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg",
                      "ca", "ceb", "ny", "zh-cn", "zh-tw", "co", "hr", "cs", "da", "nl",
                      "en", "eo", "et", "tl", "fi", "fr", "fy", "gl", "ka", "de", "el",
                      "gu", "ht", "ha", "haw", "he", "hi", "hmn", "hu", "is", "ig", "id",
                      "ga", "it", "ja", "jw", "kn", "kk", "km", "ko", "ku", "ky", "lo",
                      "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr",
                      "mn", "my", "ne", "no", "or", "ps", "fa", "pl", "pt", "pa", "ro",
                      "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so",
                      "es", "su", "sw", "sv", "tg", "ta", "te", "th", "tr", "uk", "ur",
                      "ug", "uz", "vi", "cy", "xh", "yi", "yo", "zu"]

    if not isinstance(text, str):
        raise TypeError("The text parameter must be a string.")

    if "." in filename:
        raise ValueError("The filename parameter value can't have the dot "
                         "character (.) or any file extension")

    if language not in language_codes:
        raise ValueError(f"Invalid language code: {language}")

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


def play_audio(audio_filename: str, must_delete: bool = True) -> float:
    """ Play an audio file.

        FUNCTION PARAMETERS:

        - audio_filename: string with the complete audio filename to be played, including 
    the extension;
        - must_delete(default: True): a boolean. If must_delete value is False, then the audio file
    will not be deleted after being played.

        FUNCTION LOGIC:

        After the _check_filename function is called, the mixer module from pygame is initialized.
    Then the audio_filename is loaded and played. However, since the code execution does not stop
    when mixer.music.play() is called, a while loop is necessary to wait until mixer.music.get_busy()
    returns 0, which indicates that the audio has finished being played. The total audio time will 
    be saved in a variable called seconds. Then the mixer is closed and the _delete_audio() function 
    is called.

        FUNCTION RETURN: seconds (a float)
    """
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

    return seconds


def say(text: str, *,
        filename: str = "temp",
        language: str = "en",
        slow: bool = False,
        must_delete: bool = True) -> None:
    """ Make Python read the text parameter value aloud by calling first create_audio() and
    then play_audio().

        FUNCTION PARAMETERS:

        - text: string to be read aloud; raise a TypeError if argument is not a string;
        - filename(default: "temp"): string with the audio filename. IMPORTANT: no dot 
    character should appear in the filename value. Otherwise, a ValueError will be raised 
    by the first if statement in the function body;
        - language(default: "en"): string with the acronym of the language to be used to convert
    the text parameter to audio; if the language parameter value is not in the LANGUAGE_CODES list, inside
    create_audio(), raise a ValueError;
        - slow(default: False): a boolean. If True, the created audio will be pronounced more slowly.
        - must_delete(default: True): a boolean. If must_delete value is False, then the audio file
    won't be deleted after being played.

        "text" is the only positional parameter. All the other ones must be passed to the function
    as keyword arguments.

        FUNCTION LOGIC:

        create_audio() is called, generating the audio file and returning the filename, which will be saved
    again in an audio_filename variable. Then play_audio() is called and... MAGIC! Now you can hear the text
    you used as the say function input.

        FUNCTION RETURN: None
    """
    audio_filename = create_audio(text, filename=filename,
                                  language=language, slow=slow)
    play_audio(audio_filename, must_delete)


def main(arguments_list: Union[List[str], None] = None) -> None:
    """ Call the say() function by using, as its arguments, either the sys.argv[1:]
    list or a list of strings created by the user, which will be appended to sys.argv.

        MAIN FUNCTION PARAMETER:

        - arguments_list(default: None): Either a list of strings or None. In the 
    former case, the list of strings must have the following format (example using the 
    say function all possible arguments)

            ["This is the text argument" 
            "audio_filename=name_of_the_file" 
            "language=pt" 
            "slow=True"
            "must_delete=False']

        These same "arguments as strings" can be passed when the module is executed from
    the comand line, like in the following example (one should write this code without
    line breaks in the command line):

            python -m duckytie "This is the text argument" 
                               "audio_filename=name_of_the_file" 
                               "language=pt" 
                               "slow=True"
                               "must_delete=False'


        MAIN FUNCTION LOGIC:

        A main() function is usually called with no argument and that will be its
    most common use here. In that case, the sys.argv[1:] list will be passed to
    the say() function.
        If len(sys.argv) == 2 is True, the say() function will receive sys.argv[1] 
    as its text argument, maintaining all the keywords arguments as default.
        If len(sys.argv) > 2 is True, the main() function will check if the keyword
    arguments for say() were passed correctly and, if that is not the case, a
    ValueError will be raised. Otherwise, the parameters dictionary will be updated
    with the sys.argv elements values, preparing the final call to say()
        Finally, in the else case, len(sys.argv) <= 1 is True and a couple of text 
    messages are read aloud, including the opening lines from How I Met Your Mother's
    "Ducky Tie" episode. There is here a try/except structure in this part of the code,
    treating an InterruptKeyboard exception, in case the user wants to abort the main()
    function execution.

        FUNCTION RETURN: None.
    """
    if arguments_list:
        sys.argv += arguments_list

    try:
        if len(sys.argv) == 2:
            say(sys.argv[1])

        elif len(sys.argv) > 2:
            parameters = {
                "audio_filename": "temp",
                "language": "en",
                "slow": False,
                "must_delete": True
            }

            for argument in sys.argv[2:]:
                if "=" not in argument:
                    error_message = ('There is at least one keyword argument, in the '
                                     'say() function, which was passed as a positional one. Use the '
                                     'following example to pass strings as keywords arguments in the '
                                     'command line:\n\n\t'
                                     'python -m duckytie "This is the text argument" '
                                     '"audio_filename=name_of_the_file" '
                                     '"language=pt" "slow=True" "must_delete=False\n')
                    raise ValueError(error_message)
                else:
                    parameter_name, value = argument.split("=", maxsplit=1)
                    parameters[parameter_name] = value

            say(sys.argv[1],
                audio_filename=parameters["audio_filename"],
                language=parameters["language"],
                slow=parameters["slow"],
                must_delete=parameters["must_delete"])

        else:
            transcript = """
            Marshall Ericksen says:
            Hey, what do you guys think of my new ducky tie?
            Pretty cute, right?
            And not that much more expensive than a regular tie.
            """

            say(transcript)

            time.sleep(1)

            say("The ducky tie team has a special message for you.\n"
                "Remember: you are worthy of love!")

            time.sleep(1)

            say("This is the main module. This program has finished. Thanks for running it!")

    except KeyboardInterrupt:
        print("Program was interrupted by the user.")
