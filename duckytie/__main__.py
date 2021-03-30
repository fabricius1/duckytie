from duckytie import say
import time
import sys


def main():
    try:
        if len(sys.argv) > 1:
            for argument in sys.argv[1:]:
                say(argument)

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


if __name__ == "__main__":
    main()
