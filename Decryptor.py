import pyfiglet

# ask user for input
input_text = input('\033[1m' + "Type the Encrypted text: " + '\033[0m')
# replace corresponding symbols *, &, #, +, !
new_text = input_text.replace('*', 'a').replace('&', 'e').replace('#', 'i').replace('+', 'o').replace('!', 'u')
# print output
print('\033[1m' + pyfiglet.figlet_format(new_text, font = "standard"))