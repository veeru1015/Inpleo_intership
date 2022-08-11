#Veeru Senthil
#Morse Code

#This is something I have been wanting to try for a while

#Found this dictionary on the internet

Mcd = { 'A':'.-', 'B':'-...',  'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
'1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
'0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

def encoder (text):
    text = text.upper()

    encMes = ''

    #Iterates through message
    for x in text:
        if x == ' ':
            print('  ')
#If there is a space in text, standard morse code notation has 2 spaces or dah pause
        else:
#Prints encoded morse then standard space if there is not a space
            enc += Mcd[x] + ' '
    print(enc)


message = input('Enter any message you want to be decrypted into morse code notation:')

print('Original Message: ' + message)

print()

encoder(message)



