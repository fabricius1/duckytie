# <div align="center" font-size=10em><b> THE DUCKYTIE PROJECT </b></div>

<img align="center" src="https://images-na.ssl-images-amazon.com/images/I/61PtuBcRM7L._AC_UX425_.jpg">

## Project description

Duckytie is a Python library whose main resource is the say() function, which allows to easily create code to read texts aloud. It was built by using the gtts, pygame and pydub libraries, so we are greatful to their development teams for such an amazing work.


## Installation

Install duckytie via pip:

```
pip install duckytie
```


## Recommended import statement patterns

The best way to import the duckytie.say function is with the following code:

```
from duckytie import say
```

If you want to import all the module, or if "say" is already in your namespace, we recommend you to use the following aliases (especially the first one):

```
import duckytie as tie

# OR:

import duckytie as cute

# OR:

import duckytie as swarley
```


## Quick start

You can try duckytie by running the following code. This will make the computer use the Voice from Google Translate to say out loud the respective strings:

```
# This program says hello and asks for my name.
from duckytie import say

say('Hello, world!')
say('What is your name?')    # ask for their name
myName = input("Enter your name here: ")
say('It is good to meet you, ' + myName)
say('The length of your name is ' + str(len(myName)))
say('What is your age?')    # ask for their age
myAge = input("Enter your age here: ")
say('You will be ' + str(int(myAge) + 1) + ' in a year.')
```
**Credits:** code adaped from hello.py, written and published by Al Sweigart in his great book *Automate the Boring Stuff With Python* (check the chapter complete content in https://automatetheboringstuff.com/2e/chapter1/). All the calls to the print() function were changed to the say() function from duckytie. Some other minor changes to the original code were also made. This will make the computer use the google translate assistance voice to say out loud all the strings instead of only printing them to the console.

## Release History
0.2.6<br>
CHANGE: added docstrings and README. main() function allows to run code from the command line.

0.2.5<br>
CHANGE: first version of main()

0.2.4<br>
CHANGE: first version working fine but with no documentation


IMPORTANT NOTE: versions 0.2.3 and lower don't work at all and should not be used

## Meta
Author: Fabrício Brasil
* Email: fabriciusbr@gmail.com
* Github: https://github.com/fabricius1
* LinkedIn: https://www.linkedin.com/in/fabriciobrasil/
* Medium: https://fabriciusbr.medium.com/

Distributed under the MIT license. See `LICENSE.txt` for more information.

Github project repository: https://github.com/fabricius1/duckytie