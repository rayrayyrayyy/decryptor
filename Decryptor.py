import pyfiglet
from termcolor import colored, cprint

print_yellow = lambda x: cprint(x, 'yellow')
print_red = lambda x: cprint(x, 'red')

# ask user for input
print('\n' + '=====' * 25)
input_text = input('\033[1m' + "Type the Encrypted text: " + '\033[0m')
# replace corresponding symbols *, &, #, +, !
new_text = input_text.replace('*', 'a').replace('&', 'e').replace('#', 'i').replace('+', 'o').replace('!', 'u')

print_red("\nDECRYPTING, PLEASE WAIT" + "\033[5m...\n")
import time
time.sleep (3)

# print output
print('`````' * 25)
print_yellow('\033[1m' + pyfiglet.figlet_format(new_text, font = "standard"))
print('`````' * 25)