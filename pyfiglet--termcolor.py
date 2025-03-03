#
import pyfiglet
from termcolor import colored

ascii_art = pyfiglet.figlet_format("Hello World")
colored_ascii_art = colored(ascii_art, 'blue')

print(colored_ascii_art)