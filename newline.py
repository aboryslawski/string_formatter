from itertools import islice
import pyperclip

initial_text = pyperclip.paste()
def format_text(initial_text):
    counter = 0
    array = initial_text.split("\n")   
    final_string = 'strKomenda1 =  _ \n "' + array[0] + '" & vbCrLf _'
    for i in islice(array, 1, None):
        if not i == '':
            final_string = final_string + '\n&"' + i 
            if not counter == 11:
                final_string = final_string + '" & vbCrLf _'
            else:
                final_string = final_string + '"\n\n' + 'strKomenda1 = strKomenda1 & vbCrLf _ ' 
                counter = 0
            counter = counter + 1
    if len(array) > 1:
        final_string = final_string[:-1]
    print(final_string)
    write_file(final_string)

def write_file(copy_me):
    pyperclip.copy(copy_me)

format_text(pyperclip.paste())
