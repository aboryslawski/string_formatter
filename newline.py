from itertools import islice
import pyperclip

name_of_the_file = pyperclip.paste()
def format_text(name_of_the_file):    
    array = name_of_the_file.split("\n")   
    final_string = 'SQLstring =  _ \n "' + array[0] + '"'
    for i in islice(array, 1, None):
        if not i == '':
            final_string = final_string + '\n& "' + i + '" _'
    if len(array) > 1:
        final_string = final_string[:-1]
    print(final_string)
    write_file(final_string)

def write_file(copy_me):
    pyperclip.copy(copy_me)

format_text(pyperclip.paste())
