# Created on 7 Nov 2016
# Created by: Matthew Lourenco
# This program compares two strings

def compare(input_string1, input_string2):
    input_string1 = input_string1.upper()
    input_string2 = input_string2.upper()
    
    if input_string1 == input_string2:
        return True
    else:
        return False

string1 = raw_input('Input the first string: ')
string1 = str(string1)
string2 = raw_input('Input the second string: ')
string2 = str(string2)
equal = compare(string1, string2)
if equal == True:
    print('"' + string1 + '"' + ' and ' + '"' + string2 + '"' + ' are the same.')
elif equal == False:
    print('"' + string1 + '"' + ' and ' + '"' + string2 + '"' + ' are not the same.')
